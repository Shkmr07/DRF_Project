# DRF_Project

## API Overview

This API allows you to manage campaigns and donations. Below are the endpoints available:

- **Swagger UI**
  - **Endpoint:** `GET /api/swagger/`
  - **Description:** Access the interactive Swagger UI to explore and test the API endpoints.

- **ReDoc**
  - **Endpoint:** `GET /api/redoc/`
  - **Description:** View the ReDoc API documentation, which provides a clean and detailed presentation of the API schema and endpoints.

- **Campaigns**
  - `POST /api/campaign/`: Create a new campaign
  - `PUT /api/campaign/`: Update an existing campaign
  - `DELETE /api/campaign/`: Delete a campaign
  - `POST /api/campaign/{id}/`: Create a new campaign by ID
  - `PUT /api/campaign/{id}/`: Update an existing campaign by ID
  - `DELETE /api/campaign/{id}/`: Delete a campaign by ID
  - `GET /api/campaignlist/`: List all campaigns

- **Donations**
  - `POST /api/donation/`: Create a new donation
  - `PUT /api/donation/`: Update an existing donation
  - `DELETE /api/donation/`: Delete a donation
  - `POST /api/donation/{id}/`: Create a new donation by ID
  - `PUT /api/donation/{id}/`: Update an existing donation by ID
  - `DELETE /api/donation/{id}/`: Delete a donation by ID
  - `GET /api/donationlist/`: List all donations

- **User Authentication**
  - `POST /api/login/`: Log in a user
  - `POST /api/logout/`: Log out a user
  - `POST /api/register/`: Register a new user

## Detailed API Documentation

For a detailed and interactive API documentation, please visit the following link:

[API Documentation](https://username.github.io/repo-name/redoc.html)
