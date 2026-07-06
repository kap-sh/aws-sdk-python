"""Generated from Smithy shape ``com.amazonaws.glue#GetIntegrationResourcePropertyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.string512


class GetIntegrationResourcePropertyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_glue.types.string512.String512"
    """<p>The connection ARN of the source, or the database ARN of the target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIntegrationResourcePropertyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIntegrationResourcePropertyRequest:
    out: GetIntegrationResourcePropertyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "GetIntegrationResourcePropertyRequest.resource_arn required"
        )
    return out
