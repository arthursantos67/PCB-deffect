# 🔍 PCB Defect Detection with YOLOv11

## 📜 Descrição

Este projeto tem como objetivo implementar um modelo de **detecção automática de defeitos em placas de circuito impresso (PCBs)** utilizando a arquitetura **YOLOv11**.  

O modelo foi treinado e avaliado utilizando o dataset **PCB Defects**, disponível no Kaggle. A detecção automática permite uma inspeção eficiente, ágil e precisa, reduzindo custos e erros humanos no processo de verificação de qualidade.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- 🧠 **YOLOv11 (Ultralytics)**
- 🐍 **Python**
- 🔧 **OpenCV**
- 🎨 **Albumentations (Aumento de dados)**
- 📈 **Matplotlib e Seaborn (Visualização)**
- 🎛️ **Gradio (Interface interativa)**
- 🚀 **Google Colab (Ambiente de execução)**

---

## 🔎 Defeitos Detectados

O modelo é capaz de identificar os seguintes tipos de defeitos em PCBs:

- **Missing Hole** – Buracos ausentes no circuito.
- **Mouse Bite** – Pequenos rasgos ou falhas no contorno.
- **Open Circuit** – Interrupções no circuito que causam falhas elétricas.
- **Short** – Conexões indesejadas entre condutores.
- **Spur** – Protuberâncias não planejadas no circuito.
- **Spurious Copper** – Resíduos de cobre fora do design esperado.

---

### 🔧 Dependências

Instale os pacotes necessários:

```bash
pip install ultralytics
pip install gdown
pip install albumentations
pip install gradio

