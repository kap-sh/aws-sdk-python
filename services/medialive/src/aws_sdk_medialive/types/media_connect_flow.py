"""Generated from Smithy shape ``com.amazonaws.medialive#MediaConnectFlow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class MediaConnectFlow(TypedDict):
    flow_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique ARN of the MediaConnect Flow being used as a source."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConnectFlow) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    return out


def deserialize_json(data: dict) -> MediaConnectFlow:
    out: MediaConnectFlow = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    return out
