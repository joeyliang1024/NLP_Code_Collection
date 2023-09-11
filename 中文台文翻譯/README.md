# 台文中文翻譯
- 要反向翻譯(中文->台文)只要交換欄位就好。
- 有提供白話字的資料處理。
- *OutOfMemoryError* 請調整batch size! (此環境設定為1張A100 GPU，32510MiB)。
## BART
- vocab請使用vocab.txt。
- 有重設Embedding layer (擴增後的vocab size, 768)。
- 因應任務需求，模型最大輸出調整至200，但如果只看訓練資料的話100會是最佳解。
## Transformer
- 採用idx2word, word2idx編碼。
- 調整hidden_size (same as embedding dimension)會影響模型計算需求。
## 模型結果
|  Blue Score  |Training Data|iCorpus|iCorpus 100|
| :----: | :----: | :----: | :----: |
| BART(有聖經) Man-Han | 0.3876 | 0.1240 | 0.1254 |
| BART(有聖經) Han-Man | 0.3464 | 0.1737 | 0.1773 |
| BART(無聖經) Man-Han | 0.4388 | 0.1444 | 0.1518 |
| BART(無聖經) Han-Man | 0.4324 | 0.1913 | 0.1847 |
| Transformer(有聖經) Man-Han | 0.0624 | 0.0228 | 0.0344 |
| Transformer(有聖經) Han-Man | 0.1304 | 0.0223 | 0.0370 |
| Transformer(無聖經) Man-Han | 0.0527 | 0.0138 | 0.0234 |
| Transformer(無聖經) Han-Man | 0.0807 | 0.0134 | 0.0297 |
