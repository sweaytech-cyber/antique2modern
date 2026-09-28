import json
import os

directory = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(directory, "games.json"), "r", encoding="utf-8") as f:
    games_data = json.load(f)

games_json_str = json.dumps(games_data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PK29</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-base: #09090b;
      --bg-surface: #141418;
      --bg-surface-hover: #1f1f24;
      
      --accent-white: #ffffff;
      --accent-black: #000000;
      
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(255, 255, 255, 0.22);
      --border-bright: rgba(255, 255, 255, 0.5);

      --text-primary: #ffffff;
      --text-secondary: #a1a1aa;
      --text-muted: #71717a;

      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;

      --font-sans: 'Plus Jakarta Sans', -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-base);
      color: var(--text-primary);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}

    /* Scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: var(--bg-base);
    }}
    ::-webkit-scrollbar-thumb {{
      background: rgba(255, 255, 255, 0.2);
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #ffffff;
    }}

    /* Top Bar Header */
    header {{
      position: sticky;
      top: 0;
      z-index: 50;
      background: rgba(9, 9, 11, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 0.9rem 2.2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
      text-decoration: none;
      color: var(--text-primary);
    }}

    .brand-mark {{
      width: 36px;
      height: 36px;
      border-radius: var(--radius-sm);
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1rem;
      color: #000000;
      letter-spacing: -0.5px;
    }}

    .brand-name {{
      font-weight: 800;
      font-size: 1.3rem;
      letter-spacing: -0.02em;
      color: #ffffff;
    }}

    .brand-tag {{
      font-size: 0.68rem;
      font-family: var(--font-mono);
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.06);
      color: var(--text-secondary);
      border: 1px solid var(--border-subtle);
    }}

    /* Search */
    .search-container {{
      flex: 1;
      max-width: 480px;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      padding: 0.68rem 1rem 0.68rem 2.6rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      color: var(--text-primary);
      font-size: 0.9rem;
      outline: none;
      transition: all 0.2s ease;
    }}

    .search-input:focus {{
      background: var(--bg-surface-hover);
      border-color: var(--border-bright);
      box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.15);
    }}

    .search-input::placeholder {{
      color: var(--text-muted);
    }}

    .search-icon {{
      position: absolute;
      left: 0.9rem;
      top: 50%;
      transform: translateY(-50%);
      width: 16px;
      height: 16px;
      fill: var(--text-muted);
      pointer-events: none;
    }}

    .kbd-hint {{
      position: absolute;
      right: 0.8rem;
      top: 50%;
      transform: translateY(-50%);
      font-family: var(--font-mono);
      font-size: 0.7rem;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-subtle);
      padding: 2px 6px;
      border-radius: 4px;
      pointer-events: none;
    }}

    /* Header Actions */
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.6rem 1.15rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid var(--border-subtle);
      background: var(--bg-surface);
      color: var(--text-primary);
      transition: all 0.2s ease;
      user-select: none;
    }}

    .btn:hover {{
      background: var(--bg-surface-hover);
      border-color: var(--border-hover);
      transform: translateY(-1px);
    }}

    .btn-white {{
      background: #ffffff;
      color: #000000;
      border: none;
      font-weight: 700;
    }}

    .btn-white:hover {{
      background: #e4e4e7;
      box-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
    }}

    /* Google Tab Cloak Button */
    .btn-google {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-primary);
      gap: 0.5rem;
    }}
    .btn-google:hover {{
      border-color: var(--border-hover);
      background: var(--bg-surface-hover);
    }}
    .btn-google svg {{
      flex-shrink: 0;
    }}

    /* App Main Container (Directly below Header) */
    main {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 1.8rem 2.2rem 3rem 2.2rem;
      width: 100%;
      flex: 1;
    }}

    /* Controls Bar: Categories & Counter */
    .controls-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 1.8rem;
      flex-wrap: wrap;
    }}

    .categories-ribbon {{
      display: flex;
      align-items: center;
      gap: 0.55rem;
      overflow-x: auto;
      padding-bottom: 0.3rem;
      scrollbar-width: thin;
    }}

    .cat-pill {{
      padding: 0.52rem 1.1rem;
      border-radius: var(--radius-full);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      font-size: 0.84rem;
      font-weight: 500;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }}

    .cat-pill:hover {{
      color: var(--text-primary);
      border-color: var(--border-hover);
      background: var(--bg-surface-hover);
    }}

    .cat-pill.active {{
      background: #ffffff;
      border-color: #ffffff;
      color: #000000;
      font-weight: 700;
    }}

    .meta-info {{
      font-size: 0.84rem;
      color: var(--text-muted);
      font-family: var(--font-mono);
    }}

    /* Grid Layout for Game Cards */
    .games-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
      gap: 1.3rem;
    }}

    .game-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }}

    .game-card:hover {{
      transform: translateY(-5px);
      border-color: var(--border-bright);
      background: var(--bg-surface-hover);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.7);
    }}

    /* Card Picture Image Header */
    .card-img-container {{
      width: 100%;
      height: 135px;
      position: relative;
      overflow: hidden;
      background: #18181b;
    }}

    .card-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }}

    .game-card:hover .card-img {{
      transform: scale(1.08);
    }}

    .card-img-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(9, 9, 11, 0.1) 0%, rgba(9, 9, 11, 0.75) 100%);
    }}

    /* About:blank quick launch button on card hover */
    .card-blank-btn {{
      position: absolute;
      bottom: 8px;
      left: 8px;
      padding: 4px 9px;
      border-radius: 6px;
      background: rgba(9, 9, 11, 0.82);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.18);
      color: #ffffff;
      font-size: 0.68rem;
      font-weight: 600;
      font-family: var(--font-mono);
      cursor: pointer;
      opacity: 0;
      transform: translateY(4px);
      transition: all 0.2s ease;
      z-index: 6;
      white-space: nowrap;
    }}

    .game-card:hover .card-blank-btn {{
      opacity: 1;
      transform: translateY(0);
    }}

    .card-blank-btn:hover {{
      background: rgba(255,255,255,0.18);
    }}

    .fav-star {{
      position: absolute;
      top: 8px;
      right: 8px;
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: rgba(9, 9, 11, 0.75);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      cursor: pointer;
      color: var(--text-muted);
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 5;
    }}

    .fav-star:hover {{
      transform: scale(1.15);
      background: rgba(9, 9, 11, 0.95);
      color: #ffffff;
      border-color: #ffffff;
    }}

    .fav-star.active {{
      color: #ffffff;
      border-color: #ffffff;
    }}

    .card-content {{
      padding: 0.95rem;
      display: flex;
      flex-direction: column;
      flex: 1;
      justify-content: space-between;
    }}

    .card-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-primary);
      line-height: 1.35;
      margin-bottom: 0.6rem;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .card-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: auto;
    }}

    .card-badge {{
      font-size: 0.72rem;
      color: var(--text-secondary);
      background: rgba(255, 255, 255, 0.05);
      padding: 2px 8px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
    }}

    .play-arrow {{
      width: 16px;
      height: 16px;
      fill: #ffffff;
      opacity: 0;
      transform: translateX(-4px);
      transition: all 0.25s ease;
    }}

    .game-card:hover .play-arrow {{
      opacity: 1;
      transform: translateX(0);
    }}

    /* Empty state */
    .empty-state {{
      grid-column: 1 / -1;
      padding: 4rem 2rem;
      text-align: center;
      color: var(--text-muted);
    }}

    /* Modal Player */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      z-index: 100;
      background: rgba(9, 9, 11, 0.93);
      backdrop-filter: blur(16px);
      display: flex;
      flex-direction: column;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }}

    .modal-overlay.active {{
      opacity: 1;
      pointer-events: auto;
    }}

    .modal-header {{
      padding: 0.85rem 1.8rem;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .modal-title-group {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }}

    .modal-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #ffffff;
    }}

    .modal-actions {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .iframe-container {{
      flex: 1;
      width: 100%;
      height: 100%;
      background: #000000;
      position: relative;
    }}

    .game-iframe {{
      width: 100%;
      height: 100%;
      border: none;
    }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--border-subtle);
      padding: 1.4rem 2.2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: var(--text-muted);
      font-size: 0.84rem;
      background: var(--bg-surface);
      margin-top: auto;
    }}

    footer span {{
      color: var(--text-secondary);
    }}

    /* ============================================================
       SETTINGS PANEL
    ============================================================ */
    .settings-overlay {{
      position: fixed;
      inset: 0;
      z-index: 200;
      background: rgba(0,0,0,0.55);
      backdrop-filter: blur(6px);
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.22s ease;
      display: flex;
      align-items: flex-start;
      justify-content: flex-end;
    }}

    .settings-overlay.active {{
      opacity: 1;
      pointer-events: auto;
    }}

    .settings-panel {{
      width: 380px;
      max-width: 95vw;
      height: 100vh;
      background: #111114;
      border-left: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      transform: translateX(100%);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      overflow-y: auto;
    }}

    .settings-overlay.active .settings-panel {{
      transform: translateX(0);
    }}

    .settings-header {{
      padding: 1.4rem 1.6rem 1.1rem;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      background: #111114;
      z-index: 10;
    }}

    .settings-header h2 {{
      font-size: 1.1rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.02em;
    }}

    .settings-close {{
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }}

    .settings-close:hover {{
      color: #fff;
      border-color: var(--border-hover);
      background: var(--bg-surface-hover);
    }}

    .settings-body {{
      padding: 1.4rem 1.6rem;
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }}

    .settings-section {{}}

    .settings-section-label {{
      font-size: 0.72rem;
      font-family: var(--font-mono);
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-bottom: 0.85rem;
    }}

    .settings-group {{
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }}

    /* Radio / Option rows */
    .settings-option {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.7rem 1rem;
      border-radius: var(--radius-md);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      cursor: pointer;
      transition: all 0.18s ease;
    }}

    .settings-option:hover {{
      border-color: var(--border-hover);
      background: var(--bg-surface-hover);
    }}

    .settings-option.selected {{
      border-color: #ffffff;
      background: rgba(255,255,255,0.06);
    }}

    .settings-option-left {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-size: 0.88rem;
      font-weight: 500;
      color: var(--text-primary);
    }}

    .settings-option-icon {{
      width: 28px;
      height: 28px;
      border-radius: 7px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      background: rgba(255,255,255,0.07);
      flex-shrink: 0;
    }}

    .settings-radio {{
      width: 16px;
      height: 16px;
      border-radius: 50%;
      border: 2px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s ease;
      flex-shrink: 0;
    }}

    .settings-option.selected .settings-radio {{
      border-color: #ffffff;
      background: #ffffff;
    }}

    .settings-option.selected .settings-radio::after {{
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #000000;
    }}

    /* Input fields in settings */
    .settings-input {{
      width: 100%;
      padding: 0.65rem 0.95rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      color: var(--text-primary);
      font-size: 0.88rem;
      font-family: var(--font-sans);
      outline: none;
      transition: all 0.2s ease;
    }}

    .settings-input:focus {{
      border-color: var(--border-bright);
      background: var(--bg-surface-hover);
    }}

    .settings-input::placeholder {{
      color: var(--text-muted);
    }}

    .settings-input-label {{
      font-size: 0.8rem;
      color: var(--text-secondary);
      margin-bottom: 0.4rem;
      font-weight: 500;
    }}

    .settings-field {{
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }}

    /* Full-width action button */
    .settings-btn {{
      width: 100%;
      padding: 0.75rem 1rem;
      border-radius: var(--radius-md);
      background: #ffffff;
      color: #000000;
      border: none;
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: var(--font-sans);
    }}

    .settings-btn:hover {{
      background: #e4e4e7;
      transform: translateY(-1px);
      box-shadow: 0 4px 16px rgba(255,255,255,0.15);
    }}

    .settings-btn.secondary {{
      background: var(--bg-surface);
      color: var(--text-primary);
      border: 1px solid var(--border-subtle);
    }}

    .settings-btn.secondary:hover {{
      background: var(--bg-surface-hover);
      border-color: var(--border-hover);
      box-shadow: none;
    }}

    /* Divider */
    .settings-divider {{
      height: 1px;
      background: var(--border-subtle);
      margin: 0 -1.6rem;
    }}

    @media (max-width: 640px) {{
      header {{
        padding: 0.8rem 1rem;
        flex-wrap: wrap;
      }}
      .search-container {{
        order: 3;
        max-width: 100%;
      }}
      main {{
        padding: 1rem;
      }}
      .games-grid {{
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
        gap: 0.9rem;
      }}
      .card-img-container {{
        height: 110px;
      }}
      .settings-panel {{
        width: 100vw;
      }}
    }}
  </style>
</head>
<body>

  <header>
    <a href="#" class="brand" onclick="filterCategory('All')">
      <div class="brand-mark">PK</div>
      <span class="brand-name">PK29</span>
      <span class="brand-tag">v2.0</span>
    </a>

    <div class="search-container">
      <svg class="search-icon" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
      <input type="text" id="searchInput" class="search-input" placeholder="Search 700+ unblocked games..." oninput="handleSearch()">
      <span class="kbd-hint">/</span>
    </div>

    <div class="header-actions">
      <!-- Google Tab Cloak Button -->
      <button class="btn btn-google" onclick="activateGoogleCloak()" title="Disguise this tab as Google">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
          <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
          <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
          <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
        </svg>
        Google
      </button>

      <!-- Settings Button -->
      <button class="btn" onclick="openSettings()" title="Settings">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="3"/>
          <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>
        </svg>
        Settings
      </button>
    </div>
  </header>

  <main>
    <div class="controls-bar">
      <div class="categories-ribbon" id="categoriesRibbon"></div>
      <div class="meta-info" id="metaInfo">774 games</div>
    </div>

    <div class="games-grid" id="gamesGrid"></div>
  </main>

  <footer>
    <span>PK29 Vault • Stealth Black &amp; White Edition</span>
    <span>Use <kbd style="font-family:var(--font-mono)">/</kbd> to search</span>
  </footer>

  <!-- ================================================
       GAME MODAL PLAYER
  ================================================ -->
  <div class="modal-overlay" id="gameModal">
    <div class="modal-header">
      <div class="modal-title-group">
        <span class="modal-title" id="modalTitle">Game</span>
        <span class="card-badge" id="modalCategory">Category</span>
      </div>
      <div class="modal-actions">
        <button class="btn" onclick="openCurrentGameInBlank()" title="Open in about:blank stealth tab">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          Stealth
        </button>
        <button class="btn" onclick="reloadIframe()">Reload</button>
        <button class="btn" onclick="popOutGame()">Pop Out</button>
        <button class="btn" onclick="toggleFullscreen()">Fullscreen</button>
        <button class="btn" style="border-color: rgba(239,68,68,0.3); color: #ef4444;" onclick="closeModal()">Close</button>
      </div>
    </div>
    <div class="iframe-container">
      <iframe id="gameIframe" class="game-iframe" allowfullscreen src=""></iframe>
    </div>
  </div>

  <!-- ================================================
       SETTINGS PANEL
  ================================================ -->
  <div class="settings-overlay" id="settingsOverlay" onclick="handleSettingsOverlayClick(event)">
    <div class="settings-panel" id="settingsPanel">

      <div class="settings-header">
        <h2>⚙ Settings</h2>
        <button class="settings-close" onclick="closeSettings()">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>

      <div class="settings-body">

        <!-- TAB CLOAK -->
        <div class="settings-section">
          <div class="settings-section-label">Tab Cloak</div>
          <div class="settings-group" id="cloakOptions">
            <div class="settings-option selected" onclick="selectCloak(this,'Google','https://www.google.com/favicon.ico')" data-title="Google" data-icon="https://www.google.com/favicon.ico">
              <div class="settings-option-left">
                <div class="settings-option-icon">
                  <img src="https://www.google.com/favicon.ico" width="16" height="16" style="border-radius:3px" onerror="this.style.display='none'">
                </div>
                Google
              </div>
              <div class="settings-radio"></div>
            </div>
            <div class="settings-option" onclick="selectCloak(this,'Google Classroom','https://ssl.gstatic.com/classroom/favicon.png')" data-title="Google Classroom" data-icon="https://ssl.gstatic.com/classroom/favicon.png">
              <div class="settings-option-left">
                <div class="settings-option-icon">
                  <img src="https://ssl.gstatic.com/classroom/favicon.png" width="16" height="16" style="border-radius:3px" onerror="this.style.display='none'">
                </div>
                Google Classroom
              </div>
              <div class="settings-radio"></div>
            </div>
            <div class="settings-option" onclick="selectCloak(this,'Canvas – Dashboard','https://www.instructure.com/favicon.ico')" data-title="Canvas – Dashboard" data-icon="https://www.instructure.com/favicon.ico">
              <div class="settings-option-left">
                <div class="settings-option-icon">
                  <img src="https://www.instructure.com/favicon.ico" width="16" height="16" style="border-radius:3px" onerror="this.style.display='none'">
                </div>
                Canvas Dashboard
              </div>
              <div class="settings-radio"></div>
            </div>
            <div class="settings-option" onclick="selectCloak(this,'Google Docs','https://ssl.gstatic.com/docs/documents/images/kix-favicon7.ico')" data-title="Google Docs" data-icon="https://ssl.gstatic.com/docs/documents/images/kix-favicon7.ico">
              <div class="settings-option-left">
                <div class="settings-option-icon">
                  <img src="https://ssl.gstatic.com/docs/documents/images/kix-favicon7.ico" width="16" height="16" style="border-radius:3px" onerror="this.style.display='none'">
                </div>
                Google Docs
              </div>
              <div class="settings-radio"></div>
            </div>
            <div class="settings-option" id="cloakCustomOpt" onclick="selectCloak(this,'','')">
              <div class="settings-option-left">
                <div class="settings-option-icon">✏️</div>
                Custom
              </div>
              <div class="settings-radio"></div>
            </div>
          </div>

          <!-- Custom cloak inputs -->
          <div id="customCloakFields" style="display:none; margin-top:0.75rem; display:flex; flex-direction:column; gap:0.55rem; display:none;">
            <div class="settings-field">
              <div class="settings-input-label">Custom Tab Title</div>
              <input type="text" class="settings-input" id="customCloakTitle" placeholder="e.g. Math Homework">
            </div>
            <div class="settings-field">
              <div class="settings-input-label">Custom Favicon URL</div>
              <input type="text" class="settings-input" id="customCloakIcon" placeholder="https://example.com/favicon.ico">
            </div>
          </div>

          <button class="settings-btn secondary" style="margin-top:0.75rem;" onclick="applyTabCloak()">Apply Cloak Now</button>
          <button class="settings-btn secondary" style="margin-top:0.45rem;" onclick="removeTabCloak()">Remove Cloak</button>
        </div>

        <div class="settings-divider"></div>

        <!-- AUTO CLOAK -->
        <div class="settings-section">
          <div class="settings-section-label">Auto Cloak</div>
          <div class="settings-group" id="autoCloakOptions">
            <div class="settings-option selected" onclick="selectAutoCloak(this,'off')">
              <div class="settings-option-left">
                <div class="settings-option-icon">🚫</div>
                Off
              </div>
              <div class="settings-radio"></div>
            </div>
            <div class="settings-option" onclick="selectAutoCloak(this,'about:blank')">
              <div class="settings-option-left">
                <div class="settings-option-icon">🔲</div>
                about:blank
              </div>
              <div class="settings-radio"></div>
            </div>
            <div class="settings-option" onclick="selectAutoCloak(this,'blob')">
              <div class="settings-option-left">
                <div class="settings-option-icon">🫧</div>
                blob:
              </div>
              <div class="settings-radio"></div>
            </div>
          </div>
          <button class="settings-btn" style="margin-top:0.75rem;" onclick="openSiteInBlank()">
            Open Cloaked Tab
          </button>
        </div>

        <div class="settings-divider"></div>

        <!-- PANIC KEY -->
        <div class="settings-section">
          <div class="settings-section-label">Panic Key</div>
          <div class="settings-group" style="gap:0.55rem;">
            <div class="settings-field">
              <div class="settings-input-label">Panic Shortcut Key</div>
              <input type="text" class="settings-input" id="panicKeyInput" placeholder="e.g. Escape, F1, ~" maxlength="20"
                     value="" style="font-family:var(--font-mono)">
            </div>
            <div class="settings-field">
              <div class="settings-input-label">Redirect URL</div>
              <input type="text" class="settings-input" id="panicUrlInput" placeholder="https://classroom.google.com">
            </div>
            <button class="settings-btn secondary" onclick="savePanicKey()">Save Panic Key</button>
          </div>
        </div>

        <div class="settings-divider"></div>

        <!-- OPEN SITE OPTIONS -->
        <div class="settings-section">
          <div class="settings-section-label">Site Tools</div>
          <div class="settings-group" style="gap:0.45rem;">
            <button class="settings-btn secondary" onclick="openSiteInBlank()">Open Site in about:blank</button>
            <button class="settings-btn secondary" onclick="openSiteInBlob()">Open Site in blob: URL</button>
          </div>
        </div>

      </div><!-- /settings-body -->
    </div><!-- /settings-panel -->
  </div><!-- /settings-overlay -->

  <script>
    const ALL_GAMES = {games_json_str};
    let currentCategory = 'All';
    let favorites = new Set(JSON.parse(localStorage.getItem('pk29_favs') || '[]'));
    let activeGame = null;

    // Settings state
    let selectedCloakTitle = 'Google';
    let selectedCloakIcon  = 'https://www.google.com/favicon.ico';
    let selectedAutoCloak  = 'off';
    let panicKey = localStorage.getItem('pk29_panicKey') || '';
    let panicUrl = localStorage.getItem('pk29_panicUrl') || 'https://classroom.google.com';

    const CATEGORIES = ['All', 'Featured', 'Action', 'Racing', 'Sports', 'Horror', 'Sandbox', 'Puzzle & Idle', 'Platformer', 'Arcade & Casual'];

    document.addEventListener('DOMContentLoaded', () => {{
      renderCategories();
      renderGames(ALL_GAMES);

      // Restore saved panic key values
      document.getElementById('panicKeyInput').value = panicKey;
      document.getElementById('panicUrlInput').value = panicUrl;

      document.addEventListener('keydown', (e) => {{
        // Search shortcut
        if (e.key === '/' && document.activeElement.tagName !== 'INPUT') {{
          e.preventDefault();
          document.getElementById('searchInput').focus();
        }}
        // Escape closes modal/settings
        if (e.key === 'Escape') {{
          closeModal();
          closeSettings();
        }}
        // Panic key
        if (panicKey && e.key === panicKey) {{
          window.location.href = panicUrl || 'https://classroom.google.com';
        }}
      }});
    }});

    // ============================================================
    // CATEGORIES + SEARCH
    // ============================================================
    function renderCategories() {{
      const ribbon = document.getElementById('categoriesRibbon');
      ribbon.innerHTML = CATEGORIES.map(cat => `
        <button class="cat-pill ${{cat === currentCategory ? 'active' : ''}}" onclick="filterCategory('${{cat}}')">
          ${{cat}}
        </button>
      `).join('');
    }}

    function filterCategory(cat) {{
      currentCategory = cat;
      renderCategories();
      document.getElementById('searchInput').value = '';
      
      let filtered = ALL_GAMES;
      if (cat === 'Featured') filtered = ALL_GAMES.filter(g => g.featured);
      else if (cat !== 'All') filtered = ALL_GAMES.filter(g => g.category === cat);

      renderGames(filtered);
    }}

    function handleSearch() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const filtered = ALL_GAMES.filter(g => 
        g.name.toLowerCase().includes(query) || 
        g.category.toLowerCase().includes(query) ||
        g.file.toLowerCase().includes(query)
      );
      renderGames(filtered);
    }}

    function renderGames(games) {{
      const grid = document.getElementById('gamesGrid');
      document.getElementById('metaInfo').textContent = `${{games.length}} games`;

      if (games.length === 0) {{
        grid.innerHTML = `<div class="empty-state">No games found</div>`;
        return;
      }}

      grid.innerHTML = games.map(g => {{
        const isFav = favorites.has(g.id);
        return `
          <div class="game-card" onclick="openModal('${{g.id}}')">
            <div class="card-img-container">
              <img class="card-img" src="${{g.image}}" alt="${{g.name}}" loading="lazy" onerror="this.src='https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=500&auto=format&fit=crop'">
              <div class="card-img-overlay"></div>
              <button class="card-blank-btn" onclick="event.stopPropagation(); openGameInBlank('${{g.id}}')" title="Open in stealth tab">
                ↗ Stealth
              </button>
              <button class="fav-star ${{isFav ? 'active' : ''}}" onclick="event.stopPropagation(); toggleFavorite('${{g.id}}')">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="${{isFav ? 'currentColor' : 'none'}}" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
              </button>
            </div>
            <div class="card-content">
              <span class="card-title">${{g.name}}</span>
              <div class="card-footer">
                <span class="card-badge">${{g.category}}</span>
                <svg class="play-arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    // ============================================================
    // FAVORITES
    // ============================================================
    function toggleFavorite(id) {{
      if (favorites.has(id)) favorites.delete(id);
      else favorites.add(id);
      localStorage.setItem('pk29_favs', JSON.stringify([...favorites]));
      
      const query = document.getElementById('searchInput').value;
      if (query) handleSearch();
      else filterCategory(currentCategory);
    }}

    // ============================================================
    // MODAL PLAYER
    // ============================================================
    function openModal(id) {{
      const g = ALL_GAMES.find(item => item.id === id);
      if (!g) return;
      activeGame = g;

      document.getElementById('modalTitle').textContent = g.name;
      document.getElementById('modalCategory').textContent = g.category;
      document.getElementById('gameIframe').src = g.file;
      document.getElementById('gameModal').classList.add('active');
    }}

    function closeModal() {{
      document.getElementById('gameModal').classList.remove('active');
      document.getElementById('gameIframe').src = '';
      activeGame = null;
    }}

    function reloadIframe() {{
      if (activeGame) document.getElementById('gameIframe').src = activeGame.file;
    }}

    function popOutGame() {{
      if (activeGame) window.open(activeGame.file, '_blank');
    }}

    function toggleFullscreen() {{
      const wrapper = document.querySelector('.iframe-container');
      if (!document.fullscreenElement) {{
        if (wrapper.requestFullscreen) wrapper.requestFullscreen();
      }} else {{
        if (document.exitFullscreen) document.exitFullscreen();
      }}
    }}

    // ============================================================
    // ABOUT:BLANK / STEALTH LAUNCH
    // ============================================================
    function openGameInBlank(id) {{
      const g = ALL_GAMES.find(item => item.id === id);
      if (!g) return;
      const gameUrl = window.location.origin + '/' + g.file;
      const w = window.open('about:blank', '_blank');
      if (!w) {{ alert('Pop-up blocked! Allow pop-ups for this site.'); return; }}
      w.document.write(`<!DOCTYPE html><html><head><title>Google</title><link rel="icon" href="https://www.google.com/favicon.ico"></head><body style="margin:0;padding:0;background:#000;"><iframe src="${{gameUrl}}" style="width:100vw;height:100vh;border:none;" allowfullscreen></iframe></body></html>`);
      w.document.close();
    }}

    function openCurrentGameInBlank() {{
      if (activeGame) openGameInBlank(activeGame.id);
    }}

    function openSiteInBlank() {{
      const siteUrl = window.location.href;
      const cloakTitle = selectedCloakTitle || 'Google';
      const cloakIcon  = selectedCloakIcon  || 'https://www.google.com/favicon.ico';
      const w = window.open('about:blank', '_blank');
      if (!w) {{ alert('Pop-up blocked! Allow pop-ups for this site.'); return; }}
      w.document.write(`<!DOCTYPE html><html><head><title>${{cloakTitle}}</title><link rel="icon" href="${{cloakIcon}}"></head><body style="margin:0;padding:0;"><iframe src="${{siteUrl}}" style="width:100vw;height:100vh;border:none;" allowfullscreen></iframe></body></html>`);
      w.document.close();
      closeSettings();
    }}

    function openSiteInBlob() {{
      const cloakTitle = selectedCloakTitle || 'Google';
      const cloakIcon  = selectedCloakIcon  || 'https://www.google.com/favicon.ico';
      const siteUrl    = window.location.href;
      const htmlStr = `<!DOCTYPE html><html><head><title>${{cloakTitle}}</title><link rel="icon" href="${{cloakIcon}}"></head><body style="margin:0;padding:0;"><iframe src="${{siteUrl}}" style="width:100vw;height:100vh;border:none;" allowfullscreen></iframe></body></html>`;
      const blob = new Blob([htmlStr], {{ type: 'text/html' }});
      const url  = URL.createObjectURL(blob);
      window.open(url, '_blank');
      closeSettings();
    }}

    // ============================================================
    // GOOGLE TAB CLOAK (header button)
    // ============================================================
    function activateGoogleCloak() {{
      applyCloak('Google', 'https://www.google.com/favicon.ico');
    }}

    function applyCloak(title, iconUrl) {{
      document.title = title;
      let link = document.querySelector("link[rel~='icon']");
      if (!link) {{
        link = document.createElement('link');
        link.rel = 'icon';
        document.head.appendChild(link);
      }}
      link.href = iconUrl;
    }}

    function removeTabCloak() {{
      applyCloak('PK29', '');
    }}

    // ============================================================
    // SETTINGS PANEL
    // ============================================================
    function openSettings() {{
      document.getElementById('settingsOverlay').classList.add('active');
    }}

    function closeSettings() {{
      document.getElementById('settingsOverlay').classList.remove('active');
    }}

    function handleSettingsOverlayClick(e) {{
      // Close if clicking the dark backdrop (not the panel itself)
      if (e.target === document.getElementById('settingsOverlay')) closeSettings();
    }}

    // Tab Cloak selection
    function selectCloak(el, title, icon) {{
      document.querySelectorAll('#cloakOptions .settings-option').forEach(o => o.classList.remove('selected'));
      el.classList.add('selected');

      const isCustom = (el.id === 'cloakCustomOpt');
      document.getElementById('customCloakFields').style.display = isCustom ? 'flex' : 'none';

      if (!isCustom) {{
        selectedCloakTitle = title;
        selectedCloakIcon  = icon;
      }}
    }}

    function applyTabCloak() {{
      const isCustomSelected = document.getElementById('cloakCustomOpt').classList.contains('selected');
      let title = selectedCloakTitle;
      let icon  = selectedCloakIcon;
      if (isCustomSelected) {{
        title = document.getElementById('customCloakTitle').value || 'Google';
        icon  = document.getElementById('customCloakIcon').value  || 'https://www.google.com/favicon.ico';
        selectedCloakTitle = title;
        selectedCloakIcon  = icon;
      }}
      applyCloak(title, icon);
    }}

    // Auto Cloak selection
    function selectAutoCloak(el, mode) {{
      document.querySelectorAll('#autoCloakOptions .settings-option').forEach(o => o.classList.remove('selected'));
      el.classList.add('selected');
      selectedAutoCloak = mode;
    }}

    // Panic Key
    function savePanicKey() {{
      panicKey = document.getElementById('panicKeyInput').value.trim();
      panicUrl = document.getElementById('panicUrlInput').value.trim() || 'https://classroom.google.com';
      localStorage.setItem('pk29_panicKey', panicKey);
      localStorage.setItem('pk29_panicUrl', panicUrl);
      
      // Visual feedback
      const btn = event.target;
      const original = btn.textContent;
      btn.textContent = '✓ Saved!';
      setTimeout(() => btn.textContent = original, 1500);
    }}
  </script>
</body>
</html>
"""

with open(os.path.join(directory, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("Regenerated index.html — Google Cloak + Settings Panel added.")
