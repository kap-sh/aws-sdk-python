"""Generated from Smithy shape ``com.amazonaws.glue#GetIntegrationTablePropertiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.string128
    import aws_sdk_glue.types.string512


class GetIntegrationTablePropertiesRequest(TypedDict):
    resource_arn: "aws_sdk_glue.types.string512.String512"
    """<p>The Amazon Resource Name (ARN) of the target table for which to retrieve integration table properties. Currently, this API only supports retrieving properties for target tables, and the provided ARN should be the ARN of the target table in the Glue Data Catalog. Support for retrieving integration table properties for source connections (using the connection ARN) is not yet implemented and will be added in a future release. </p>"""
    table_name: "aws_sdk_glue.types.string128.String128"
    """<p>The name of the table to be replicated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIntegrationTablePropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIntegrationTablePropertiesRequest:
    out: GetIntegrationTablePropertiesRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "GetIntegrationTablePropertiesRequest.resource_arn required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "GetIntegrationTablePropertiesRequest.table_name required"
        )
    return out
