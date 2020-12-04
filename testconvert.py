import unittest
import convert

ifyourehappyandyouknowitv1_nh = '''Wolitahasiyin cokoptihik!
Wolitahasiyin cokoptihik!
Wolitahasiyin, wolitahasiyin
Wolitahasiyin cokoptihik!

Wolitahasiyin likonahpus!
Wolitahasiyin likonahpus!
Wolitahasiyin, wolitahasiyin
Wolitahasiyin likonahpus!

Wolitahasiyin kakalu  "'Tahu!"
Wolitahasiyin kakalu  "'Tahu!"
Wolitahasiyin, wolitahasiyin
Wolitahasiyin kakalu "'Tahu!"

Wolitahasiyin psiw-te keq olluhken!
Wolitahasiyin psiw-te keq olluhken!
Wolitahasiyin, wolitahasiyin
Wolitahasiyin psiw-te keq olluhken!

Wolitahasiyin cokoptihik, likonahpus, kakalu "'Tahu!"
Wolitahasiyin cokoptihik, likonahpus, kakalu "'Tahu!"
Wolitahasiyin, wolitahasiyin
Wolitahasiyin cokoptihik, likonahpus, kakalu "'Tahu!"'''
        
ifyourehappyandyouknowitv1_t = '''Wəlitahasiyin cəkəptihik!
Wəlitahasiyin cəkəptihik!
Wəlitahasiyin, Wəlitahasiyin
Wəlitahasiyin cəkəptihik!

Wəlitahasiyin likənahpos!
Wəlitahasiyin likənahpos!
Wəlitahasiyin, Wəlitahasiyin
Wəlitahasiyin likənahpos!

Wəlitahasiyin kakalo  "'Taho!"
Wəlitahasiyin kakalo  "'Taho!"
Wəlitahasiyin, Wəlitahasiyin
Wəlitahasiyin kakalo "'Taho!"

Wəlitahasiyin psiw-te kekw əllohken!
Wəlitahasiyin psiw-te kekw əllohken!
Wəlitahasiyin, Wəlitahasiyin
Wəlitahasiyin psiw-te kekw əllohken!

Wəlitahasiyin cəkəptihik, likənahpos, kakalo "'Taho!"
Wəlitahasiyin cəkəptihik, likənahpos, kakalo "'Taho!"
Wəlitahasiyin, Wəlitahasiyin
Wəlitahasiyin cəkəptihik, likənahpos, kakalo "'Taho!"'''

# If you're happy and you know it version 2 is not available for
# Newell-Hale (it's there, but it doesn't link to the right file).


# NOTE: Removed a duplicate white space on two lines in this text to make it
# match the newell-hale example
ifyourehappyandyouknowitv3_t = '''Wəlitahasiyin naka 'kəcicihton cəkəptihik!
Wəlitahasiyin naka 'kəcicihton cəkəptihik!
Wəlitahasiyin naka 'kəcicihton
Wəlitahasiyin naka 'kəcicihton
Wəlitahasiyin naka 'kəcicihton cəkəptihik!

Wəlitahasiyin naka 'kəcicihton likənahpos!
Wəlitahasiyin naka 'kəcicihton likənahpos!
Wəlitahasiyin naka 'kəcicihton
Wəlitahasiyin naka 'kəcicihton
Wəlitahasiyin naka 'kəcicihton likənahpos!

Wəlitahasiyin naka 'kəcicihton kakalo "'Taho!"
Wəlitahasiyin naka 'kəcicihton kakalo "'Taho!"
Wəlitahasiyin naka 'kəcicihton
Wəlitahasiyin naka 'kəcicihton
Wəlitahasiyin naka 'kəcicihton kakalo "'Taho!"

Wəlitahasiyin naka 'kəcicihton cəkəptihik, likənahpos, kakalo "'Taho!"
Wəlitahasiyin naka 'kəcicihton cəkəptihik, likənahpos, kakalo "'Taho!"
Wəlitahasiyin naka 'kəcicihton
Wəlitahasiyin naka 'kəcicihton
Wəlitahasiyin naka 'kəcicihton cəkəptihik, likənahpos, kakalo "'Taho!"'''

ifyourehappyandyouknowitv3_nh = '''Wolitahasiyin naka 'kocicihtun cokoptihik!
Wolitahasiyin naka 'kocicihtun cokoptihik!
Wolitahasiyin naka 'kocicihtun
Wolitahasiyin naka 'kocicihtun
Wolitahasiyin naka 'kocicihtun cokoptihik!

Wolitahasiyin naka 'kocicihtun likonahpus!
Wolitahasiyin naka 'kocicihtun likonahpus!
Wolitahasiyin naka 'kocicihtun
Wolitahasiyin naka 'kocicihtun
Wolitahasiyin naka 'kocicihtun likonahpus!

Wolitahasiyin naka 'kocicihtun kakalu "'Tahu!"
Wolitahasiyin naka 'kocicihtun kakalu "'Tahu!"
Wolitahasiyin naka 'kocicihtun
Wolitahasiyin naka 'kocicihtun
Wolitahasiyin naka 'kocicihtun kakalu "'Tahu!"

Wolitahasiyin naka 'kocicihtun cokoptihik, likonahpus, kakalu "'Tahu!"
Wolitahasiyin naka 'kocicihtun cokoptihik, likonahpus, kakalu "'Tahu!"
Wolitahasiyin naka 'kocicihtun
Wolitahasiyin naka 'kocicihtun
Wolitahasiyin naka 'kocicihtun cokoptihik, likonahpus, kakalu "'Tahu!"'''

# I'm a little teapot available for NH, but not for Teeter.

itsbitsspiderv1_t = '''Apsbkilbk Amoshbpihk
Apsbkilbk amoshbpihk ’tewepatowan
Sblahkiw kbmiwbn naka notiyelikwan
Notahan kisohs, 'kispaston samakwan
Bn Apsbkilbk amoshbpihk apc ’tewepatowan'''

itsbitsspiderv1_nh = '''Apsokilok Amushopihk
Apsokilok amushopihk ’tewepatuwan
Solahkiw komiwon naka nutiyeliqan
Nutahan kisuhs, 'kispastun samaqan
On Apsokilok amushopihk apc ’tewepatuwan'''

itsbitsspiderv2_t = '''Amoshbpihkbssis
Amoshbpihkbssis
Ewepatowe notecowbk
Bn ehta macelan, amoshbpihkbssis macelbkwan
Notiyahso kisohs, 'kispaston ellak
Apc amoshbpihkbssis
'Tewepatowan notecowbk'''

itsbitsspiderv2_nh = '''Amushopihkossis
Amushopihkossis
Ewepatuwe nutecuwok
On ehta macelan, amushopihkossis maceloqan
Nutiyahsu kisuhs, 'kispastun ellak
Apc amushopihkossis
'Tewepatuwan nutecuwok'''

itsbitsspiderv3_t = '''Apsbkilbk
Apsbkilbk amoshbpihk ’tewepatowan
Sblahkiw kbmiwbn naka notiyelikwan
Kisohs notahan, naka 'kispahton samakwan
Bn Apsbkilbk amoshbpihk apc
’tewepatowan'''
# This word includes a 'u', which I didn't think is valid in
# Teeter. In v1 it is spelled with an 'o' in the Teeter version
# Amushbpihk

itsbitsspiderv3_nh = '''Apsokilok
Apsokilok amushopihk ’tewepatuwan
Solahkiw komiwon naka nutiyeliqan
Kisuhs nutahan, naka 'kispahtun samaqan
On Apsokilok amushopihk apc
’tewepatuwan'''
# Amushopihk

twolittleblackbirds_t = '''Nisowək Kahkakohsək pemkwepihtit əpəmew!
Peskw liwiso Piyel, kətək liwiso Pal.
Macetowi Piyel, macetowi Pal.
Ckowi apaci Piyel, ckowi apaci Pal.
Macetowi, macetowi, macetowiyakw!'''

twolittleblackbirds_nh = '''Nisuwok kahkakuhsok pemqepihtit opomew!
Pesq liwisu Piyel, kotok liwisu Pal.
Macetuwi Piyel, macetuwi Pal.
Ckuwi apaci Piyel, ckuwi apaci Pal.
Macetuwi, macetuwi, macetuwiyaq!'''

patacake_t = '''Samtahan sokələpan notəpanket
Samtahan sokələpan notəpanket
sokələpan
Ktəpikwelan, ksamtahan
Ktowikhan “C”
Kpisahckwelan nolbmakwbsikbnbk 'ciw naka nil.'''
# NOTE: These words don't convert correctly. 
# Wisa-nolowakwsəmowin (Teeter version has an extra vowel (after kw/q))
# Cameron (Spelled differently between versions)

patacake_nh = '''Samtahan sukolopan nutopanket
Samtahan sukolopan nutopanket
sukolopan
Ktopiqelan, ksamtahan
Ktuwikhan “C”
Kpisahcqelan nulomaqosikonok 'ciw naka nil.'''
# Wisa-nuluwaqosomuwin
# Camryn

class TestConvert(unittest.TestCase):

    def test_normalize_b(self):
        self.assertEqual(convert.normalize_b('b'), 'ə')
        self.assertEqual(convert.normalize_b('B'), 'Ə')
        self.assertEqual(convert.normalize_b('Apsbkilbk'), 'Apsəkilək')
        self.assertEqual(convert.normalize_b('Bn'), 'Ən')

    def test_nh2t(self):
        # Simple tests
        self.assertEqual(convert.convert_nh2t(''), ('', []))
        self.assertEqual(convert.convert_nh2t('o'), ('ə', []))
        self.assertEqual(convert.convert_nh2t('u'), ('o', []))
        self.assertEqual(convert.convert_nh2t('O'), ('Ə', []))
        self.assertEqual(convert.convert_nh2t('U'), ('O', []))
        self.assertEqual(convert.convert_nh2t('aq'), ('akw', []))
        self.assertEqual(convert.convert_nh2t('aQ'), ('aKw', []))

        # Tests for word initial q/kw detection
        self.assertEqual(convert.convert_nh2t('q'), ('q', [0]))
        self.assertEqual(convert.convert_nh2t('Q'), ('Q', [0]))

        self.assertEqual(convert.convert_nh2t("qapit"),
                         ("qapit", [0]))
        self.assertEqual(convert.convert_nh2t("qaqeku"),
                         ("qakweko", [0]))
        self.assertEqual(convert.convert_nh2t("'qiltuwal"),
                         ("'qiltowal", [1]))
        self.assertEqual(convert.convert_nh2t("pesq qapit"),
                         ("peskw qapit", [6]))
        self.assertEqual(convert.convert_nh2t("pesq qaqeku"),
                         ("peskw qakweko", [6]))
        self.assertEqual(convert.convert_nh2t("pesq 'qiltuwal"),
                         ("peskw 'qiltowal", [7]))
        self.assertEqual(convert.convert_nh2t("qapit 'qiltuwal"),
                         ("qapit 'qiltowal", [0,7]))

        # Tests from skicinowato
        # Note: There are casing differences between the NH and T versions
        self.assertEqual(convert.convert_nh2t(ifyourehappyandyouknowitv1_nh.lower()),
                         (ifyourehappyandyouknowitv1_t.lower(), []))

        self.assertEqual(convert.convert_nh2t(ifyourehappyandyouknowitv3_nh),
                         (ifyourehappyandyouknowitv3_t, []))

        # Teeter version contains b's which need to be normalized
        self.assertEqual(convert.convert_nh2t(itsbitsspiderv1_nh),
                         (convert.normalize_b(itsbitsspiderv1_t), []))

        # Teeter version contains b's which need to be normalized
        self.assertEqual(convert.convert_nh2t(itsbitsspiderv2_nh),
                         (convert.normalize_b(itsbitsspiderv2_t), []))

        # Teeter version contains b's which need to be normalized
        # This test fails. The Teeter text contains a 'u'... I didn't
        # think this letter was used in the Teeter system.
        self.assertEqual(convert.convert_nh2t(itsbitsspiderv3_nh),
                         (convert.normalize_b(itsbitsspiderv3_t), []))

        self.assertEqual(convert.convert_nh2t(patacake_nh),
                         (convert.normalize_b(patacake_t), []))

    def test_t2nh(self):
        self.assertEqual(convert.convert_t2nh(''), ('', []))
        self.assertEqual(convert.convert_t2nh('ə'), ('o', []))
        self.assertEqual(convert.convert_t2nh('o'), ('u', []))
        self.assertEqual(convert.convert_t2nh('Ə'), ('O', []))
        self.assertEqual(convert.convert_t2nh('O'), ('U', []))
        self.assertEqual(convert.convert_t2nh('akw'), ('aq', []))
        self.assertEqual(convert.convert_t2nh('aKw'), ('aQ', []))

        # Tests for word initial q/kw detection
        self.assertEqual(convert.convert_t2nh('kw'), ('kw', [0, 1]))
        self.assertEqual(convert.convert_t2nh('Kw'), ('Kw', [0, 1]))

        self.assertEqual(convert.convert_t2nh("kwapit"),
                         ("kwapit", [0, 1]))
        self.assertEqual(convert.convert_t2nh("kwakweko"),
                         ("kwaqeku", [0, 1]))
        self.assertEqual(convert.convert_t2nh("'kwiltowal"),
                         ("'kwiltuwal", [1, 2]))
        self.assertEqual(convert.convert_t2nh("peskw kwapit"),
                         ("pesq kwapit", [5, 6]))
        self.assertEqual(convert.convert_t2nh("peskw kwakweko"),
                         ("pesq kwaqeku", [5, 6]))
        self.assertEqual(convert.convert_t2nh("peskw 'kwiltowal"),
                         ("pesq 'kwiltuwal", [6, 7]))
        self.assertEqual(convert.convert_t2nh("kwapit 'kwiltowal"),
                         ("kwapit 'kwiltuwal", [0, 1, 8, 9]))


        # Note: There are casing differences between the NH and T versions
        self.assertEqual(convert.convert_t2nh(ifyourehappyandyouknowitv1_t.lower()),
                         (ifyourehappyandyouknowitv1_nh.lower(), []))

        self.assertEqual(convert.convert_t2nh(ifyourehappyandyouknowitv3_t),
                         (ifyourehappyandyouknowitv3_nh, []))

        self.assertEqual(convert.convert_t2nh(itsbitsspiderv1_t),
                         (itsbitsspiderv1_nh, []))

        self.assertEqual(convert.convert_t2nh(itsbitsspiderv2_t),
                         (itsbitsspiderv2_nh, []))

        self.assertEqual(convert.convert_t2nh(itsbitsspiderv3_t),
                         (itsbitsspiderv3_nh, []))

        self.assertEqual(convert.convert_t2nh(patacake_t),
                         (patacake_nh, []))

if __name__ == '__main__':
    unittest.main()
