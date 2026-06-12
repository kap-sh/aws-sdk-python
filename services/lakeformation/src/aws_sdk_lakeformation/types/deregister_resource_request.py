"""Generated from Smithy shape ``com.amazonaws.lakeformation#DeregisterResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.resource_arn_string


class DeregisterResourceRequest(TypedDict):
    resource_arn: "aws_sdk_lakeformation.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DeregisterResourceRequest:
    out: DeregisterResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("DeregisterResourceRequest.resource_arn required")
    return out
