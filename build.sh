#!/bin/bash
set -e

echo "Starting build process..."
echo "Current directory: $(pwd)"

# Navigate to the app directory with Chinese characters
APP_DIR="Kimi_Agent_古董二现代网站/app"

echo "App directory: $APP_DIR"
cd "$APP_DIR"

echo "Installing dependencies..."
npm install --legacy-peer-deps

echo "Building project..."
npm run build

echo "Build completed successfully!"
ls -la dist/

cd ../..
echo "Build artifacts ready for deployment"
