"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DeleteStageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.stage_arn


class DeleteStageRequest(TypedDict, closed=True):
    arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStageRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteStageRequest:
    out: DeleteStageRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteStageRequest.arn required")
    return out
