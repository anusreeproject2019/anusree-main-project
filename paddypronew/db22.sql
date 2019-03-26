/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - paddy
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`paddy` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `paddy`;

/*Table structure for table `admin_full_report` */

DROP TABLE IF EXISTS `admin_full_report`;

CREATE TABLE `admin_full_report` (
  `frepo_id` int(11) NOT NULL AUTO_INCREMENT,
  `crop` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `noof_disease` bigint(20) DEFAULT NULL,
  `symptoms` varchar(50) DEFAULT NULL,
  `action` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`frepo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `admin_full_report` */

insert  into `admin_full_report`(`frepo_id`,`crop`,`place`,`noof_disease`,`symptoms`,`action`) values 
(2,'paddy','balussery',3,'fghjkk','awdf'),
(3,'abcdef','ggyyhj',8,'vgkuh','dtrt');

/*Table structure for table `article_add` */

DROP TABLE IF EXISTS `article_add`;

CREATE TABLE `article_add` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `article_title` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `file` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `article_add` */

/*Table structure for table `farmer_reg` */

DROP TABLE IF EXISTS `farmer_reg`;

CREATE TABLE `farmer_reg` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `house` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `phone` bigint(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `panchayath` varchar(50) DEFAULT NULL,
  `landmark` varchar(50) DEFAULT NULL,
  `crop` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `owner` varchar(50) DEFAULT NULL,
  `document` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `farmer_reg` */

insert  into `farmer_reg`(`fid`,`fname`,`gender`,`house`,`place`,`address`,`district`,`phone`,`email`,`panchayath`,`landmark`,`crop`,`type`,`owner`,`document`) values 
(1,'Aswathi','female','pullissery','narikkuni','abcd','kozhikode',9367898765,'achu@gmail.com','kakkodi','fghjk','paddy','fdtyui','werty','asdfghkllo'),
(2,'Amrutha','female','manoli','beypore','xyz','kozhikode',9253678935,'anu@gmail.com','beypore','qazxswedc','paddy','mkijnbhu','oqmzja','qqweertyy');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `fid` int(11) DEFAULT NULL,
  `farmer_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `panchayath` varchar(50) DEFAULT NULL,
  `disease` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`fid`,`farmer_name`,`place`,`panchayath`,`disease`,`time`,`feedback`) values 
(1,2,'Amrutha','beypore','beypore','ertyyu','10:08:00','dfghjkl');

/*Table structure for table `fertilizer_details` */

DROP TABLE IF EXISTS `fertilizer_details`;

CREATE TABLE `fertilizer_details` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `additional_info` varchar(50) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fertilizer_details` */

/*Table structure for table `govt_policies` */

DROP TABLE IF EXISTS `govt_policies`;

CREATE TABLE `govt_policies` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `policy_name` varchar(50) DEFAULT NULL,
  `subject` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `govt_policies` */

insert  into `govt_policies`(`pid`,`policy_name`,`subject`,`description`,`date`) values 
(1,'aaaaaaaa','abcdef','pqrst','2019-03-12');

/*Table structure for table `krishibhavan_reg` */

DROP TABLE IF EXISTS `krishibhavan_reg`;

CREATE TABLE `krishibhavan_reg` (
  `kid` int(11) NOT NULL,
  `officer_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `panchayath` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`kid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `krishibhavan_reg` */

insert  into `krishibhavan_reg`(`kid`,`officer_name`,`email`,`phone`,`post`,`district`,`panchayath`,`pincode`) values 
(2,'Diljith','diljith@gmail.com','9245678987','officer','Kozhikode','Puramery','612345'),
(6,'Arathi','arathi@gmail.com','9456785678','officer','Wayanad','Chorode','673015');

/*Table structure for table `krishibhavan_report` */

DROP TABLE IF EXISTS `krishibhavan_report`;

CREATE TABLE `krishibhavan_report` (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `fid` int(11) DEFAULT NULL,
  `farmer_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `crop` varchar(50) DEFAULT NULL,
  `disease` varchar(50) DEFAULT NULL,
  `applied_pesticide` varchar(50) DEFAULT NULL,
  `applied_fertilizer` varchar(50) DEFAULT NULL,
  `detailed_report` varchar(50) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `krishibhavan_report` */

insert  into `krishibhavan_report`(`report_id`,`fid`,`farmer_name`,`place`,`crop`,`disease`,`applied_pesticide`,`applied_fertilizer`,`detailed_report`,`photo`) values 
(1,2,'Amrutha','beypore','paddy','black','rtyu','zxcvv','qwertyuioop','gftrfr');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`type`,`username`,`password`) values 
(1,'admin','admin','admin');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `disease` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `plant` varchar(50) DEFAULT NULL,
  `symptoms` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

/*Table structure for table `pesticide_details` */

DROP TABLE IF EXISTS `pesticide_details`;

CREATE TABLE `pesticide_details` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `additional_info` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `pesticide_details` */

/*Table structure for table `seed_info` */

DROP TABLE IF EXISTS `seed_info`;

CREATE TABLE `seed_info` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `additional_info` varchar(50) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `seed_info` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
