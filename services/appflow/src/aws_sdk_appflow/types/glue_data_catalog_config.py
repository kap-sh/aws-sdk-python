"""Generated from Smithy shape ``com.amazonaws.appflow#GlueDataCatalogConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.glue_data_catalog_database_name
    import aws_sdk_appflow.types.glue_data_catalog_iam_role
    import aws_sdk_appflow.types.glue_data_catalog_table_prefix


class GlueDataCatalogConfig(TypedDict, closed=True):
    role_arn: "aws_sdk_appflow.types.glue_data_catalog_iam_role.GlueDataCatalogIAMRole"
    r"""<p>The Amazon Resource Name (ARN) of an IAM role that grants Amazon AppFlow the permissions it needs to create Data Catalog tables, databases, and partitions.</p> <p>For an example IAM policy that has the required permissions, see <a href=\"https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_id-based-policy-examples.html\">Identity-based policy examples for Amazon AppFlow</a>.</p>"""
    database_name: "aws_sdk_appflow.types.glue_data_catalog_database_name.GlueDataCatalogDatabaseName"
    """<p>The name of the Data Catalog database that stores the metadata tables that Amazon AppFlow creates in your Amazon Web Services account. These tables contain metadata for the data that's transferred by the flow that you configure with this parameter.</p> <note> <p>When you configure a new flow with this parameter, you must specify an existing database.</p> </note>"""
    table_prefix: "aws_sdk_appflow.types.glue_data_catalog_table_prefix.GlueDataCatalogTablePrefix"
    """<p>A naming prefix for each Data Catalog table that Amazon AppFlow creates for the flow that you configure with this setting. Amazon AppFlow adds the prefix to the beginning of the each table name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueDataCatalogConfig) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["databaseName"] = value["database_name"]
    out["tablePrefix"] = value["table_prefix"]
    return out


def deserialize_json(data: dict) -> GlueDataCatalogConfig:
    out: GlueDataCatalogConfig = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GlueDataCatalogConfig.role_arn required")
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError("GlueDataCatalogConfig.database_name required")
    if "tablePrefix" in data:
        out["table_prefix"] = data["tablePrefix"]
    else:
        raise DeserializationError("GlueDataCatalogConfig.table_prefix required")
    return out
