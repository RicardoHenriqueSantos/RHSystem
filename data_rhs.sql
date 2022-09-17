CREATE DATABASE  IF NOT EXISTS `db_vendas` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_vendas`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: db_vendas
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionario` (
  `fun_cod` int NOT NULL AUTO_INCREMENT,
  `fun_nome` varchar(50) DEFAULT NULL,
  `fun_senha` int DEFAULT NULL,
  PRIMARY KEY (`fun_cod`)
) ENGINE=InnoDB AUTO_INCREMENT=20220905 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario`
--

LOCK TABLES `funcionario` WRITE;
/*!40000 ALTER TABLE `funcionario` DISABLE KEYS */;
INSERT INTO `funcionario` VALUES (20220902,'Henrique Silva',202209),(20220903,'Paula Braga',202210),(20220904,'César Oliveira',202211);
/*!40000 ALTER TABLE `funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produto`
--

DROP TABLE IF EXISTS `produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produto` (
  `prod_cod` int NOT NULL AUTO_INCREMENT,
  `prod_item` varchar(70) DEFAULT NULL,
  `prod_marca` varchar(40) DEFAULT NULL,
  `prod_custo` float DEFAULT NULL,
  `prod_venda` float DEFAULT NULL,
  `prod_tipo` varchar(30) DEFAULT NULL,
  `prod_estoque` int DEFAULT NULL,
  PRIMARY KEY (`prod_cod`)
) ENGINE=InnoDB AUTO_INCREMENT=810 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produto`
--

LOCK TABLES `produto` WRITE;
/*!40000 ALTER TABLE `produto` DISABLE KEYS */;
INSERT INTO `produto` VALUES (777,'Camiseta Glory Of The Holy One','Valiant Of David',39.99,79.99,'Camiseta',74),(778,'Camiseta Hear The Lion Roar','Valiant Of David',39.99,79.99,'Camiseta',71),(779,'Camiseta King Of Kings','Valiant Of David',39.99,79.99,'Camiseta',36),(780,'Camiseta Solomon','Valiant Of David',39.99,79.99,'Camiseta',20),(781,'Bota Desert Wanderer','Journey',129.99,323,'Calçados',11),(782,'Bible Vintage Black NVI','Dominus Vobiscum',38.89,59.9,'Livros',5),(783,'Livro - O Ceticismo da Fé','Ágape',39.9,55.8,'Livros',11),(805,'Camiseta Fly Like A Eagle','Consulado do Rock',49.99,90,'Camiseta',18),(806,'Camiseta Edu Falaschi - Vera Cruz','Consulado do Rock',49.99,90,'Camiseta',9),(809,'Colar Cross','Cross',10,18,'Acessório',42);
/*!40000 ALTER TABLE `produto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venda`
--

DROP TABLE IF EXISTS `venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venda` (
  `ven_cod` int NOT NULL AUTO_INCREMENT,
  `ven_data` varchar(10) DEFAULT NULL,
  `ven_total` float DEFAULT NULL,
  `ven_cod_fun` int DEFAULT NULL,
  `ven_cod_produto` int DEFAULT NULL,
  `ven_quant` int DEFAULT NULL,
  PRIMARY KEY (`ven_cod`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venda`
--

LOCK TABLES `venda` WRITE;
/*!40000 ALTER TABLE `venda` DISABLE KEYS */;
INSERT INTO `venda` VALUES (9,'12/09/2022',59.9,20220902,782,1),(10,'12/09/2022',159.98,20220902,777,2),(11,'12/09/2022',323,20220902,781,1),(12,'12/09/2022',323,20220902,781,1),(13,'12/09/2022',323,20220902,781,1),(14,'12/09/2022',159.98,20220902,778,2),(15,'13/09/2022',79.99,20220902,780,1),(16,'13/09/2022',79.99,20220902,780,1),(17,'13/09/2022',79.99,20220902,780,1),(18,'13/09/2022',323,20220902,781,1),(19,'13/09/2022',89,20220902,805,1),(20,'13/09/2022',79.99,20220903,777,1),(21,'13/09/2022',59.9,20220903,782,1),(22,'13/09/2022',89,20220902,805,1),(23,'13/09/2022',79.99,20220902,778,1),(24,'13/09/2022',90,20220902,806,1),(25,'13/09/2022',79.99,20220902,780,1),(26,'14/09/2022',159.98,20220902,777,2),(27,'14/09/2022',59.9,20220902,782,1),(28,'14/09/2022',111.6,20220904,783,2),(29,'14/09/2022',79.99,20220904,778,1),(30,'14/09/2022',159.98,20220903,777,2),(31,'14/09/2022',55.8,20220902,783,1),(32,'14/09/2022',299.5,20220902,782,5),(33,'14/09/2022',239.97,20220904,777,3),(34,'15/09/2022',55.8,20220902,783,1),(35,'15/09/2022',969,20220902,781,3),(36,'15/09/2022',450,20220902,806,5),(37,'15/09/2022',646,20220902,781,2),(38,'15/09/2022',144,20220902,809,8);
/*!40000 ALTER TABLE `venda` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-17 10:52:48
