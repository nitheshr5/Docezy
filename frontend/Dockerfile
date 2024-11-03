# Use a Node.js image to build and serve the app
FROM node:16-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY ./package.json ./package-lock.json ./
RUN npm install

# Copy all files and build
COPY . .
RUN npm run build

# Expose the port for the frontend app
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
