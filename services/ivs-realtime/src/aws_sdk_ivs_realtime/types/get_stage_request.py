"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetStageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.stage_arn


class GetStageRequest(TypedDict):
    arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage for which the information is to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStageRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetStageRequest:
    out: GetStageRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetStageRequest.arn required")
    return out
