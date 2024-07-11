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

# MAGIC %sh 
# MAGIC
# MAGIC mkdir /tmp/test/test
# MAGIC cd /Workspace/Repos/.internal/acfc8a97f5_commits/d11290e82172358c6516203b173174044dc5aacd/
# MAGIC cp -r * /tmp/test/test/
# MAGIC cd /tmp/test/test/
# MAGIC
# MAGIC #cd /Workspace/Repos/praveenkumar.pathak@databricks.com/test_repo_for_dbk_support
# MAGIC pip install ./

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -l  /tmp/test/test/build/lib/t

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /Workspace/Repos/.internal/f82fad67e9_commits/0ac35f4ddb497eb7dceb0a5a60c44c7641090278
# MAGIC ls -l .
# MAGIC python3 setup.py bdist_wheel
# MAGIC

# COMMAND ----------

ls -l

# COMMAND ----------

# MAGIC %sh
# MAGIC pip install wheel setuptools

# COMMAND ----------


cd /Workspace/Repos/.internal/acfc8a97f5_commits/d11290e82172358c6516203b173174044dc5aacd/
pip install ./

# COMMAND ----------

# MAGIC %sh pwd

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -la /Workspace/Repos/

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -la /Workspace/Repos/.internal/acfc8a97f5_commits/d11290e82172358c6516203b173174044dc5aacd/*

# COMMAND ----------


