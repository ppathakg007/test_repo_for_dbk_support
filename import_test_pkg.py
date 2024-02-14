# Databricks notebook source
# MAGIC %sh pwd

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -l ./test_pkg/test_method.py
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC cat ./test_pkg/test_method.py

# COMMAND ----------

# MAGIC %pip install ./

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -l /Workspace/Repos/.internal/f82fad67e9_commits/0ac35f4ddb497eb7dceb0a5a60c44c7641090278/

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /Workspace/Repos/.internal/f82fad67e9_commits/0ac35f4ddb497eb7dceb0a5a60c44c7641090278
# MAGIC ls -l .
# MAGIC python3 setup.py bdist_wheel
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC pip install wheel setuptools

# COMMAND ----------

l
