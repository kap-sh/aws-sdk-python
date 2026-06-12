"""Generated from Smithy shape ``com.amazonaws.glue#DataLakeAccessProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean
    import aws_sdk_glue.types.iam_role_arn
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.resource_arn_string


class DataLakeAccessProperties(TypedDict):
    data_lake_access: "aws_sdk_glue.types.boolean.Boolean"
    """<p>Turns on or off data lake access for Apache Spark applications that access Amazon Redshift databases in the Data Catalog from any non-Redshift engine, such as Amazon Athena, Amazon EMR, or Glue ETL.</p>"""
    data_transfer_role: NotRequired["aws_sdk_glue.types.iam_role_arn.IAMRoleArn"]
    """<p>A role that will be assumed by Glue for transferring data into/out of the staging bucket during a query.</p>"""
    kms_key: NotRequired["aws_sdk_glue.types.resource_arn_string.ResourceArnString"]
    """<p>An encryption key that will be used for the staging bucket that will be created along with the catalog.</p>"""
    catalog_type: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Specifies a federated catalog type for the native catalog resource. The currently supported type is <code>aws:redshift</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataLakeAccessProperties) -> dict:
    out: dict = {}
    out["DataLakeAccess"] = value.get("data_lake_access", False)
    if "data_transfer_role" in value:
        out["DataTransferRole"] = value["data_transfer_role"]
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    if "catalog_type" in value:
        out["CatalogType"] = value["catalog_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataLakeAccessProperties:
    out: DataLakeAccessProperties = {}  # type: ignore[typeddict-item]
    if "DataLakeAccess" in data:
        out["data_lake_access"] = data["DataLakeAccess"]
    else:
        out["data_lake_access"] = False
    if "DataTransferRole" in data:
        out["data_transfer_role"] = data["DataTransferRole"]
    if "KmsKey" in data:
        out["kms_key"] = data["KmsKey"]
    if "CatalogType" in data:
        out["catalog_type"] = data["CatalogType"]
    return out
