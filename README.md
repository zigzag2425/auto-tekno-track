# 🎛️ Auto Techno Track Generator

Un générateur automatique de track **Techno Tribe / Acidcore** inspiré de la culture Free Party (150–180 BPM), en Python.  
Il crée un morceau complet (drums, bassline, leads, breaks, arrangement, mixage) jusqu’à un **fichier de set `.als` simulé** pour Ableton Live.

---

## 🚀 Fonctionnalités

- ✅ Génération de patterns techno / acid :
  - Kick 4/4
  - Bassline acid TB-303 style
  - Lead rave
  - Break percussif
- ✅ Arrangement automatique (intro, drop, break, outro)
- ✅ Mixage automatique (velocité, dynamique simple)
- ✅ Export MIDI + création d’un fichier `.als` simulé

---

## 🧰 Prérequis

- Python ≥ 3.9
- [Ableton Live](https://www.ableton.com/)
- Python packages :
  ```bash
  pip install pretty_midi mido
  ```

---

## 📁 Structure du projet

```
auto_techno_track/
├── scripts/
│   ├── 1_generate_kick.py
│   ├── 2_generate_bassline.py
│   ├── 3_generate_lead.py
│   ├── 4_generate_break.py
│   ├── 5_arrange_track.py
│   ├── 6_auto_mix.py
│   ├── 7_export_als.py
│   └── main.py
├── output/
│   ├── midi/
│   ├── mixed/
│   └── als/
├── README.md
└── .gitignore
```

---

## ▶️ Utilisation

### 1. Cloner ou créer le projet

```bash
git clone https://github.com/ton-utilisateur/auto_techno_track.git
cd auto_techno_track
```

### 2. Exécuter tous les scripts

```bash
cd scripts
python main.py
```

Tu peux aussi exécuter les étapes une par une :
```bash
python 1_generate_kick.py
python 2_generate_bassline.py
python 3_generate_lead.py
python 4_generate_break.py
python 5_arrange_track.py
python 6_auto_mix.py
python 7_export_als.py
```

---

## 🎼 Résultat

Après exécution, tu obtiendras :

- Tous les fichiers `.mid` dans `output/midi/`
- Le morceau final mixé dans `output/mixed/freeparty_track_160bpm_auto_mix.mid`
- Un fichier `.als` simulé (zip renommé) dans `output/als/freeparty_set.als` que tu peux importer dans Ableton Live

---

## ⚠️ Remarques

- Le fichier `.als` est une **structure simulée** (Ableton n’a pas d’API officielle pour écrire des `.als` nativement).
- Tu peux importer les `.mid` dans un projet Ableton vide, les assigner à des synthés (kick, 303, breaks, etc.), et commencer le sound design.
- Tous les patterns sont générés aléatoirement à chaque exécution — idéal pour expérimenter.

---

## 🧠 Idées futures

- Génération de samples audio (kick drum generator, acid synth)
- Intégration avec Max for Live ou VST
- Contrôle via interface graphique
- Choix du BPM / style en ligne de commande

---

## 🕹️ Free Party Spirit

🔥 Ce projet est fait pour les producteurs de rave, les bidouilleurs, les passionnés d'automatisation musicale.  
Tu veux générer 50 idées de track pour une nuit de live ? Tu es au bon endroit.

Peace, Unity, Respect, Automation. ✊
