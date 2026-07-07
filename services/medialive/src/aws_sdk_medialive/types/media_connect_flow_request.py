"""Generated from Smithy shape ``com.amazonaws.medialive#MediaConnectFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class MediaConnectFlowRequest(TypedDict, closed=True):
    flow_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the MediaConnect Flow that you want to use as a source."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConnectFlowRequest) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    return out


def deserialize_json(data: dict) -> MediaConnectFlowRequest:
    out: MediaConnectFlowRequest = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    return out
