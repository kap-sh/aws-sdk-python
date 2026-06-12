"""Generated from Smithy shape ``com.amazonaws.glue#DataLakeAccessPropertiesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean
    import aws_sdk_glue.types.iam_role_arn
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.resource_arn_string


class DataLakeAccessPropertiesOutput(TypedDict):
    data_lake_access: "aws_sdk_glue.types.boolean.Boolean"
    """<p>Turns on or off data lake access for Apache Spark applications that access Amazon Redshift databases in the Data Catalog.</p>"""
    data_transfer_role: NotRequired["aws_sdk_glue.types.iam_role_arn.IAMRoleArn"]
    """<p>A role that will be assumed by Glue for transferring data into/out of the staging bucket during a query.</p>"""
    kms_key: NotRequired["aws_sdk_glue.types.resource_arn_string.ResourceArnString"]
    """<p>An encryption key that will be used for the staging bucket that will be created along with the catalog.</p>"""
    managed_workgroup_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The managed Redshift Serverless compute name that is created for your catalog resource.</p>"""
    managed_workgroup_status: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The managed Redshift Serverless compute status.</p>"""
    redshift_database_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The default Redshift database resource name in the managed compute.</p>"""
    status_message: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>A message that gives more detailed information about the managed workgroup status.</p>"""
    catalog_type: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Specifies a federated catalog type for the native catalog resource. The currently supported type is <code>aws:redshift</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataLakeAccessPropertiesOutput) -> dict:
    out: dict = {}
    out["DataLakeAccess"] = value.get("data_lake_access", False)
    if "data_transfer_role" in value:
        out["DataTransferRole"] = value["data_transfer_role"]
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    if "managed_workgroup_name" in value:
        out["ManagedWorkgroupName"] = value["managed_workgroup_name"]
    if "managed_workgroup_status" in value:
        out["ManagedWorkgroupStatus"] = value["managed_workgroup_status"]
    if "redshift_database_name" in value:
        out["RedshiftDatabaseName"] = value["redshift_database_name"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "catalog_type" in value:
        out["CatalogType"] = value["catalog_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataLakeAccessPropertiesOutput:
    out: DataLakeAccessPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "DataLakeAccess" in data:
        out["data_lake_access"] = data["DataLakeAccess"]
    else:
        out["data_lake_access"] = False
    if "DataTransferRole" in data:
        out["data_transfer_role"] = data["DataTransferRole"]
    if "KmsKey" in data:
        out["kms_key"] = data["KmsKey"]
    if "ManagedWorkgroupName" in data:
        out["managed_workgroup_name"] = data["ManagedWorkgroupName"]
    if "ManagedWorkgroupStatus" in data:
        out["managed_workgroup_status"] = data["ManagedWorkgroupStatus"]
    if "RedshiftDatabaseName" in data:
        out["redshift_database_name"] = data["RedshiftDatabaseName"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "CatalogType" in data:
        out["catalog_type"] = data["CatalogType"]
    return out
