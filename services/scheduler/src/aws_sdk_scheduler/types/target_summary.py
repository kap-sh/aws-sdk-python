"""Generated from Smithy shape ``com.amazonaws.scheduler#TargetSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.target_arn


class TargetSummary(TypedDict):
    arn: "aws_sdk_scheduler.types.target_arn.TargetArn"
    """<p>The Amazon Resource Name (ARN) of the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> TargetSummary:
    out: TargetSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("TargetSummary.arn required")
    return out
