# SNOWFLAKE STANDARDS

This document outlines the naming standards and conventions to be followed when designing and managing the Snowflake environment. The guidelines provided cover database, schema, table, column, view, and stored procedure naming strategies. It is important to note that in Snowflake, all object names, including databases, schemas, tables, columns, views, and stored procedures, must be capitalized.   

## DATABASE NAMING
- All database names must be capitalized.
- Use clear and descriptive names that reflect the segment or domain of data they contain.
- **Segment-based Naming:** Name databases based on the segment or domain of data they contain, such as:
  - **PATIENTS:** For databases containing patient demographic and health records.
  - **CLAIMS:** For databases containing insurance claims data.
  - **LAB_RESULTS:** For databases containing laboratory test results.
  - **MEDICATION:** For databases containing prescription and medication history.

## SCHEMA NAMING
- All schema names must be capitalized.
- **Types of Schemas:**
  - **RAW:** Used for storing raw data directly from source systems.
  - **DEV:** Development schema for testing and prototyping.
  - **CURATED:** Schema for curated data after cleansing and transformation.
  - **ANALYTICS:** Schema for analytical data models and reporting.

## TABLE NAMING
- All table names must be capitalized.
- Table names should reflect their content or purpose by grain, e.g., `DT_AGG_PATIENT_VISIT_HISTORY`.
- Tables follow a convention where each word is separated by an underscore, e.g., `PATIENT_ALLERGY_RECORDS`.
- **Use prefixes to indicate the type of table when necessary:**
  - **DIM (Dimension):** For tables containing dimensional data (e.g., `DIM_PATIENT`).
  - **FACT (Fact):** For tables containing fact data (e.g., `FACT_LAB_TEST_RESULTS`).
  - **OBT (One Big Table):** For tables containing observation-level data (e.g., `OBT_MEDICATION_HISTORY`).
  - **DT (Detail):** For detailed level data (e.g., `DT_PATIENT_DIAGNOSIS_DETAILS`).

## COLUMN NAMING
- All column names must be capitalized.
- Words in each column name must be separated by an underscore, e.g., `PATIENT_ID`.
- Use descriptive column names that clearly indicate the data they contain.
- Avoid using generic column names like `ID` or `NAME` unless they are universally applicable.

## VIEW NAMING
- All view names must be capitalized.
- View names should reflect their purpose or content, e.g., `ACTIVE_PATIENT_VISITS`.
- **Use prefixes to indicate the type of view when applicable:**
  - **AGG (Aggregate):** For aggregate views (e.g., `AGG_PATIENT_MEDICATION_USAGE`).
  - **SUM (Summary):** For summary views (e.g., `SUM_HOSPITAL_ADMISSIONS_BY_MONTH`).
  - **OBT (Observation):** For observation-level views (e.g., `OBT_PATIENT_DIAGNOSIS_HISTORY`).
  - **DET (Detail):** For detailed-purpose views (e.g., `DET_LAB_RESULTS_BY_PATIENT`).

## STORED PROCEDURE NAMING
- All stored procedure names must be capitalized.
- Use clear and descriptive names that reflect the purpose of the procedure.
- Prefix stored procedures with `USP` (User Stored Procedure).
- Stored procedure names must start with one of the following keywords:
  - **INC (Increment):** For procedures related to incrementing or updating data.
  - **RELOAD:** For procedures related to reloading or refreshing data.
  - **VALIDATE:** For procedures related to data validation or integrity checks.
- **Example names:**
  - `USP_INC_UPDATE_PATIENT_RECORDS`
  - `USP_RELOAD_CLAIMS_DATA`
  - `USP_VALIDATE_LAB_RESULTS`

## ROLES AND RESPONSIBILITIES

### Production Owner (Prod Owner) Role:
- Use the `PROD_OWNER` role for managing production environments such as creating and updating views and tables.
- Ensures the availability, reliability, and performance of production environments.

### System Administrator (SysAdmin) Role:
- Manages and administers the Snowflake account and infrastructure.
- Provisions resources, configures security settings, and monitors system health.
- Has higher responsibility than `PROD_OWNER`.

### Avoiding the Account Admin Role:
- Do not rely on the `ACCOUNTADMIN` role for routine tasks.
- Custom roles, such as `PROD_OWNER` and `SYSADMIN`, should be utilized for specific responsibilities.
- This ensures a more granular and secure access control model, minimizing the risk of unauthorized access or accidental data exposure.
