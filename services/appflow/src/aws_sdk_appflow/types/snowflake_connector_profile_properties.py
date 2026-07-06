"""Generated from Smithy shape ``com.amazonaws.appflow#SnowflakeConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.account_name
    import aws_sdk_appflow.types.bucket_name
    import aws_sdk_appflow.types.bucket_prefix
    import aws_sdk_appflow.types.private_link_service_name
    import aws_sdk_appflow.types.region
    import aws_sdk_appflow.types.stage
    import aws_sdk_appflow.types.warehouse


class SnowflakeConnectorProfileProperties(TypedDict, closed=True):
    warehouse: "aws_sdk_appflow.types.warehouse.Warehouse"
    """<p> The name of the Snowflake warehouse. </p>"""
    stage: "aws_sdk_appflow.types.stage.Stage"
    """<p> The name of the Amazon S3 stage that was created while setting up an Amazon S3 stage in the Snowflake account. This is written in the following format: < Database>< Schema><Stage Name>. </p>"""
    bucket_name: "aws_sdk_appflow.types.bucket_name.BucketName"
    """<p> The name of the Amazon S3 bucket associated with Snowflake. </p>"""
    bucket_prefix: NotRequired["aws_sdk_appflow.types.bucket_prefix.BucketPrefix"]
    """<p> The bucket path that refers to the Amazon S3 bucket associated with Snowflake. </p>"""
    private_link_service_name: NotRequired[
        "aws_sdk_appflow.types.private_link_service_name.PrivateLinkServiceName"
    ]
    """<p> The Snowflake Private Link service name to be used for private data transfers. </p>"""
    account_name: NotRequired["aws_sdk_appflow.types.account_name.AccountName"]
    """<p> The name of the account. </p>"""
    region: NotRequired["aws_sdk_appflow.types.region.Region"]
    """<p> The Amazon Web Services Region of the Snowflake account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeConnectorProfileProperties) -> dict:
    out: dict = {}
    out["warehouse"] = value["warehouse"]
    out["stage"] = value["stage"]
    out["bucketName"] = value["bucket_name"]
    if "bucket_prefix" in value:
        out["bucketPrefix"] = value["bucket_prefix"]
    if "private_link_service_name" in value:
        out["privateLinkServiceName"] = value["private_link_service_name"]
    if "account_name" in value:
        out["accountName"] = value["account_name"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> SnowflakeConnectorProfileProperties:
    out: SnowflakeConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "warehouse" in data:
        out["warehouse"] = data["warehouse"]
    else:
        raise DeserializationError(
            "SnowflakeConnectorProfileProperties.warehouse required"
        )
    if "stage" in data:
        out["stage"] = data["stage"]
    else:
        raise DeserializationError("SnowflakeConnectorProfileProperties.stage required")
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError(
            "SnowflakeConnectorProfileProperties.bucket_name required"
        )
    if "bucketPrefix" in data:
        out["bucket_prefix"] = data["bucketPrefix"]
    if "privateLinkServiceName" in data:
        out["private_link_service_name"] = data["privateLinkServiceName"]
    if "accountName" in data:
        out["account_name"] = data["accountName"]
    if "region" in data:
        out["region"] = data["region"]
    return out
