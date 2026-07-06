"""Generated from Smithy shape ``com.amazonaws.appflow#RedshiftConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.bucket_name
    import aws_sdk_appflow.types.bucket_prefix
    import aws_sdk_appflow.types.cluster_identifier
    import aws_sdk_appflow.types.data_api_role_arn
    import aws_sdk_appflow.types.database_name
    import aws_sdk_appflow.types.database_url
    import aws_sdk_appflow.types.role_arn
    import aws_sdk_appflow.types.workgroup_name


class RedshiftConnectorProfileProperties(TypedDict, closed=True):
    database_url: NotRequired["aws_sdk_appflow.types.database_url.DatabaseUrl"]
    """<p> The JDBC URL of the Amazon Redshift cluster. </p>"""
    bucket_name: "aws_sdk_appflow.types.bucket_name.BucketName"
    """<p> A name for the associated Amazon S3 bucket. </p>"""
    bucket_prefix: NotRequired["aws_sdk_appflow.types.bucket_prefix.BucketPrefix"]
    """<p> The object key for the destination bucket in which Amazon AppFlow places the files. </p>"""
    role_arn: "aws_sdk_appflow.types.role_arn.RoleArn"
    r"""<p> The Amazon Resource Name (ARN) of IAM role that grants Amazon Redshift read-only access to Amazon S3. For more information, and for the polices that you attach to this role, see <a href=\"https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#redshift-access-s3\">Allow Amazon Redshift to access your Amazon AppFlow data in Amazon S3</a>.</p>"""
    data_api_role_arn: NotRequired[
        "aws_sdk_appflow.types.data_api_role_arn.DataApiRoleArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of an IAM role that permits Amazon AppFlow to access your Amazon Redshift database through the Data API. For more information, and for the polices that you attach to this role, see <a href=\"https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#access-redshift\">Allow Amazon AppFlow to access Amazon Redshift databases with the Data API</a>.</p>"""
    is_redshift_serverless: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Indicates whether the connector profile defines a connection to an Amazon Redshift Serverless data warehouse.</p>"""
    cluster_identifier: NotRequired[
        "aws_sdk_appflow.types.cluster_identifier.ClusterIdentifier"
    ]
    """<p>The unique ID that's assigned to an Amazon Redshift cluster.</p>"""
    workgroup_name: NotRequired["aws_sdk_appflow.types.workgroup_name.WorkgroupName"]
    """<p>The name of an Amazon Redshift workgroup.</p>"""
    database_name: NotRequired["aws_sdk_appflow.types.database_name.DatabaseName"]
    """<p>The name of an Amazon Redshift database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftConnectorProfileProperties) -> dict:
    out: dict = {}
    if "database_url" in value:
        out["databaseUrl"] = value["database_url"]
    out["bucketName"] = value["bucket_name"]
    if "bucket_prefix" in value:
        out["bucketPrefix"] = value["bucket_prefix"]
    out["roleArn"] = value["role_arn"]
    if "data_api_role_arn" in value:
        out["dataApiRoleArn"] = value["data_api_role_arn"]
    out["isRedshiftServerless"] = value.get("is_redshift_serverless", False)
    if "cluster_identifier" in value:
        out["clusterIdentifier"] = value["cluster_identifier"]
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    return out


def deserialize_json(data: dict) -> RedshiftConnectorProfileProperties:
    out: RedshiftConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "databaseUrl" in data:
        out["database_url"] = data["databaseUrl"]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError(
            "RedshiftConnectorProfileProperties.bucket_name required"
        )
    if "bucketPrefix" in data:
        out["bucket_prefix"] = data["bucketPrefix"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "RedshiftConnectorProfileProperties.role_arn required"
        )
    if "dataApiRoleArn" in data:
        out["data_api_role_arn"] = data["dataApiRoleArn"]
    if "isRedshiftServerless" in data:
        out["is_redshift_serverless"] = data["isRedshiftServerless"]
    else:
        out["is_redshift_serverless"] = False
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    return out
