# Databricks notebook source
# COMMAND ----------

%sh pwd

# COMMAND ----------

%sh ls -l

# MAGIC %pip install .

# COMMAND ----------

import test_pkg

# COMMAND ----------

test_pkg.test_method()
