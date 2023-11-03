/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - frba
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`frba` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `frba`;

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `stud_id` int(10) DEFAULT NULL,
  `date` date NOT NULL,
  `attendance` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `attendance` */

insert  into `attendance`(`id`,`stud_id`,`date`,`attendance`) values 
(9,23,'2021-09-13',1),
(10,25,'2021-09-13',1),
(11,24,'2021-09-13',1),
(12,22,'2021-09-13',0),
(13,24,'2021-09-14',1),
(14,23,'2021-09-14',1),
(15,22,'2021-09-14',1),
(16,25,'2021-09-14',1),
(17,23,'2021-09-15',1),
(18,25,'2021-09-15',1),
(19,24,'2021-09-15',1);

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `d_name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`id`,`d_name`) values 
(1,'bca'),
(5,'bba'),
(6,'bmmc'),
(7,'bttm'),
(9,'bcom.ca');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `stud_id` int(10) DEFAULT NULL,
  `date` date NOT NULL,
  `feedback` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`id`,`stud_id`,`date`,`feedback`) values 
(1,2,'2021-08-12','ok'),
(2,3,'2021-09-09','ooh'),
(3,3,'2021-09-09','good'),
(4,3,'2021-09-09','good'),
(5,3,'2021-09-09','good'),
(6,3,'2021-09-09','good'),
(7,7,'2021-09-09','verygood'),
(8,3,'2021-09-09','Good'),
(9,3,'2021-09-10','good'),
(10,3,'2021-09-10','Good'),
(11,24,'2021-09-13','Good');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`usertype`) values 
(1,'admin','password','admin'),
(3,'hananneshrin','123456','student'),
(4,'shahma','123456','teacher'),
(5,'hananneshrin@gmail.com','123456','student'),
(6,'shakeeb123@gmail.com','123456','student'),
(7,'shahmamhd123@gmail.com','123456','student'),
(8,'shinadh123@gmail.com','123456','student'),
(9,'padmaja','123456','teacher'),
(10,'shahma','123456','teacher'),
(11,'rinshadc6@gmail.com','123456','student'),
(12,'hanan','123456','teacher'),
(13,'abc','22','parent'),
(14,'han','hanana','parent'),
(15,'vbjj','ghhg','parent'),
(16,'vbjj','ghhg','parent'),
(17,'abcde','12345','parent'),
(19,'abcdef','123456','parent'),
(21,'shahmaa','123456','parent'),
(22,'shekeebmohammed10@gmail.com','123456','student'),
(23,'hananneshrin@gmail.com','123456','student'),
(24,'shahma.mohammed@gmail.com','123456','student'),
(25,'shinadh.mohammed007@gmail.com','123456','student'),
(26,'subaida','123456','parent');

/*Table structure for table `mark` */

DROP TABLE IF EXISTS `mark`;

CREATE TABLE `mark` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `stud_id` int(10) DEFAULT NULL,
  `mark` double NOT NULL,
  `sub_id` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `mark` */

insert  into `mark`(`id`,`stud_id`,`mark`,`sub_id`) values 
(1,3,12,1),
(2,7,15,1),
(3,24,18,1),
(4,22,25,1),
(5,22,22,2);

/*Table structure for table `parent` */

DROP TABLE IF EXISTS `parent`;

CREATE TABLE `parent` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `login_id` int(10) DEFAULT NULL,
  `first_name` varchar(10) DEFAULT NULL,
  `last_name` varchar(10) DEFAULT NULL,
  `admission_number` int(10) DEFAULT NULL,
  `contact_no` bigint(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `parent` */

insert  into `parent`(`id`,`login_id`,`first_name`,`last_name`,`admission_number`,`contact_no`) values 
(1,13,'abcd','e',2,4262762836),
(2,18,'abcd','e',3,4262762836),
(3,19,'abc','def',4,123456789),
(4,20,'ab','c',5,123456789),
(5,21,'shahma','shenah',6,123456789),
(6,26,'Subaida','Mohammed',24,8070504030);

/*Table structure for table `remark` */

DROP TABLE IF EXISTS `remark`;

CREATE TABLE `remark` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `stud_id` int(10) DEFAULT NULL,
  `date` varchar(90) NOT NULL,
  `remark` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `remark` */

insert  into `remark`(`id`,`stud_id`,`date`,`remark`) values 
(1,1,'2021-08-31','good'),
(2,3,'2021-08-31','bad'),
(3,2,'2021-08-31','average'),
(4,13,'2021-08-31','excellent'),
(5,2,'2021-09-10','good');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `login_id` int(10) DEFAULT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `roll_no` int(10) NOT NULL,
  `dept_id` int(10) DEFAULT NULL,
  `semester` int(10) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `date_of_birth` date NOT NULL,
  `gender` varchar(20) NOT NULL,
  `address` varchar(50) NOT NULL,
  `district` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `pin` bigint(20) NOT NULL,
  `contactno` bigint(13) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`id`,`login_id`,`first_name`,`last_name`,`roll_no`,`dept_id`,`semester`,`photo`,`date_of_birth`,`gender`,`address`,`district`,`place`,`post`,`pin`,`contactno`) values 
(6,22,'Mohammed','Shekeeb',2,1,5,'shakeeb.jpg','2001-08-16','male','Kottola','Malappuram','Makkarapparamb','Vattallur',676507,8714535257),
(7,23,'Hanan','Neshrin',1235,1,5,'hanan.jpg','2000-06-20','female','Pathath','Malappuram','Perinthalmanna','Perinthalmanna',679322,9857534797),
(8,24,'shahma','mohammed',24,1,5,'shahma.jpg','2000-07-14','female','chettali','Malappuram','pattikkad','perinthalmanna',679322,9050407010),
(9,25,'Mohammed','Shinadh',25,1,5,'shinadh.jpg','2001-02-12','male','Padinharakam House','Malappuram','Ponnani','Ponnani',679577,8075263275);

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `sub_id` int(10) NOT NULL AUTO_INCREMENT,
  `dep_id` int(10) DEFAULT NULL,
  `sem` int(10) NOT NULL,
  `subject` varchar(30) NOT NULL,
  PRIMARY KEY (`sub_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`sub_id`,`dep_id`,`sem`,`subject`) values 
(1,1,1,'html'),
(2,1,2,'english'),
(3,1,3,'toc'),
(5,1,5,'SE');

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `teacher_id` int(10) NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `address` varchar(30) NOT NULL,
  `district` varchar(30) NOT NULL,
  `place` varchar(30) NOT NULL,
  `post` varchar(20) NOT NULL,
  `pin` bigint(10) NOT NULL,
  `contact_no` bigint(10) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `dep_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `teacher` */

insert  into `teacher`(`teacher_id`,`fname`,`lname`,`gender`,`address`,`district`,`place`,`post`,`pin`,`contact_no`,`mail`,`dep_id`) values 
(4,'shahma','mohamed','female','ALINGAL HOUSE,NARIPPARAMBU PO','malappuram','pmna','pmna',679322,36595498,'shahmamhd123@gmail.com',6),
(5,'hanan','neshrin.p','female','pathath','malappuram','perinthalmanna','perinthalmanna',679322,9874562321,'anuanna@gmail.com',9);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
