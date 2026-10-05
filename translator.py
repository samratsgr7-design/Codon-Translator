# 🧬 Project 5: Codon to Amino Acid Translator 🧬
# 🚀 PU-CET 2027 | Biotech + AI

codon_table = {
    "AUG": "Methionine (Start) 🟢 | ⭐ Essential",
    "UUU": "Phenylalanine ⚪ | ⭐ Essential",
    "UUC": "Phenylalanine ⚪ | ⭐ Essential",
    "UUA": "Leucine ⚪ | ⭐ Essential",
    "UUG": "Leucine ⚪ | ⭐ Essential",
    "CUU": "Leucine ⚪ | ⭐ Essential",
    "AUU": "Isoleucine ⚪ | ⭐ Essential",
    "GUU": "Valine ⚪ | ⭐ Essential",
    "GCU": "Alanine 🟡 | Non-essential",
    "GGU": "Glycine 🟡 | Non-essential",
    "CGU": "Arginine 🔵 | Basic +ve",
    "AAA": "Lysine 🔵 | Basic +ve | ⭐ Essential",
    "GAA": "Glutamic Acid 🔴 | Acidic -ve",
    "UAA": "STOP 🔴 | Termination",
    "UAG": "STOP 🔴 | Termination",
    "UGA": "STOP 🔴 | Termination"
}

def translate(codon):
    codon = codon.upper().strip()
    if codon in codon_table:
        return f"✅ {codon} -> {codon_table[codon]}"
    else:
        return f"❌ {codon} not found. Try AUG, UUU, UAA etc."

print("="*45)
print("🧬 CODON TRANSLATOR - DNA to Protein 🧬")
print("🚀 PU-CET | AI Drug Scientist Dream")
print("="*45)
print(translate("AUG"))
print(translate("UUU"))
print(translate("UAA"))

print("\n" + "-"*45)
user_codon = input("🔍 Enter codon (e.g. AUG): ")
print(translate(user_codon))
print("-"*45)
print("💚 Day 20 Done! Keep grinding! 🔥")
