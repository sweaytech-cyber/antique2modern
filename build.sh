#!/bin/bash
set -e

echo "=== ANTIQUE 2 MODERN DEPLOYMENT BUILD ==="
echo "Working directory: $(pwd)"

# Copy app to root level for GitHub Actions to handle cleanly
echo "Setting up build environment..."
cp -r "Kimi_Agent_古董二现代网站/app" ./app-build

cd ./app-build

echo "Installing dependencies..."
npm install --legacy-peer-deps 2>&1 | tail -5

echo "Building React app..."
npm run build 2>&1 | tail -10

echo ""
echo "✓ BUILD SUCCESSFUL"
echo "Dist folder size: $(du -sh dist/ | cut -f1)"
ls -lah dist/

exit 0
