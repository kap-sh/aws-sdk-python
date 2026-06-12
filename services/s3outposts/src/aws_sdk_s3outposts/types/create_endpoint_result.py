"""Generated from Smithy shape ``com.amazonaws.s3outposts#CreateEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3outposts.types.endpoint_arn


class CreateEndpointResult(TypedDict):
    endpoint_arn: NotRequired["aws_sdk_s3outposts.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEndpointResult) -> dict:
    out: dict = {}
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    return out


def deserialize_json(data: dict) -> CreateEndpointResult:
    out: CreateEndpointResult = {}  # type: ignore[typeddict-item]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    return out
