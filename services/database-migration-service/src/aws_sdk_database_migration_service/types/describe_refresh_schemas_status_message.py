"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeRefreshSchemasStatusMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class DescribeRefreshSchemasStatusMessage(TypedDict, closed=True):
    endpoint_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRefreshSchemasStatusMessage) -> dict:
    out: dict = {}
    out["EndpointArn"] = value["endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRefreshSchemasStatusMessage:
    out: DescribeRefreshSchemasStatusMessage = {}  # type: ignore[typeddict-item]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    else:
        raise DeserializationError(
            "DescribeRefreshSchemasStatusMessage.endpoint_arn required"
        )
    return out
