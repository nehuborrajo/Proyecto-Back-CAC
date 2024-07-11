create database portalJuegos;
use portalJuegos;

CREATE TABLE Juego (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(25) NOT NULL,
	version VARCHAR(10) NOT NULL,
	precio DECIMAL(10, 2) NOT NULL 
);