"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetHostInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.host_arn


class GetHostInput(TypedDict):
    host_arn: "aws_sdk_codeconnections.types.host_arn.HostArn"
    """<p>The Amazon Resource Name (ARN) of the requested host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetHostInput) -> dict:
    out: dict = {}
    out["HostArn"] = value["host_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetHostInput:
    out: GetHostInput = {}  # type: ignore[typeddict-item]
    if "HostArn" in data:
        out["host_arn"] = data["HostArn"]
    else:
        raise DeserializationError("GetHostInput.host_arn required")
    return out
