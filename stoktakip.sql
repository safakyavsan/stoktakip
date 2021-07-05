-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 05 Tem 2021, 06:27:24
-- Sunucu sürümü: 10.1.38-MariaDB
-- PHP Sürümü: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `stoktakip`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kategori`
--

CREATE TABLE `kategori` (
  `id` int(11) NOT NULL,
  `kategori` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `kategori`
--

INSERT INTO `kategori` (`id`, `kategori`) VALUES
(1, 'Gıda'),
(2, 'Spor'),
(3, 'Eğlence'),
(4, 'Giyim'),
(5, 'Elektronik'),
(6, 'Hediyelik'),
(7, 'Temizlik');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urunler`
--

CREATE TABLE `urunler` (
  `id` int(11) NOT NULL,
  `kategori` varchar(50) NOT NULL,
  `isim` varchar(50) NOT NULL,
  `adet` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `urunler`
--

INSERT INTO `urunler` (`id`, `kategori`, `isim`, `adet`) VALUES
(1, 'Gıda', 'Peynir', 30),
(2, 'Eğlence', 'Monopoly', 25),
(3, 'Giyim', 'Pantolon', 30),
(4, 'Elektronik', 'Iphone', 50),
(5, 'Hediyelik', 'Kitap', 50),
(6, 'Temizlik', 'Bulaşık Süngeri', 50),
(10, 'Spor', 'Forma', 15);

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `kategori`
--
ALTER TABLE `kategori`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `urunler`
--
ALTER TABLE `urunler`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `kategori`
--
ALTER TABLE `kategori`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Tablo için AUTO_INCREMENT değeri `urunler`
--
ALTER TABLE `urunler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
