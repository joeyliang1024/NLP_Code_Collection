# 中文台文二元分類
- 分類出物目標句子是中文還是台語
- 模型參數：
    1. bert_model_name = 'ckiplab/bert-base-chinese'
    2. num_classes = 2
    3. max_length = 128
    4. batch_size = 16
    5. num_epochs = 5
    6. learning_rate = 2e-5
- 模型準確度：0.93~0.94 (視Epoch數而定)    
- 資料筆數：137176筆