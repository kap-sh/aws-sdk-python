"""Generated from Smithy shape ``com.amazonaws.glue#DeleteIntegrationTablePropertiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.string128
    import aws_sdk_glue.types.string512


class DeleteIntegrationTablePropertiesRequest(TypedDict):
    resource_arn: "aws_sdk_glue.types.string512.String512"
    """<p>The connection ARN of the source, or the database ARN of the target.</p>"""
    table_name: "aws_sdk_glue.types.string128.String128"
    """<p>The name of the table to be replicated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIntegrationTablePropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIntegrationTablePropertiesRequest:
    out: DeleteIntegrationTablePropertiesRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "DeleteIntegrationTablePropertiesRequest.resource_arn required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "DeleteIntegrationTablePropertiesRequest.table_name required"
        )
    return out
