"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossFailoverSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min100


class InputLossFailoverSettings(TypedDict, closed=True):
    input_loss_threshold_msec: NotRequired[
        "aws_sdk_medialive.types.__integer_min100.__integerMin100"
    ]
    """The amount of time (in milliseconds) that no input is detected. After that time, an input failover will occur."""


# --- restJson1 ser/de ---
def serialize_json(value: InputLossFailoverSettings) -> dict:
    out: dict = {}
    if "input_loss_threshold_msec" in value:
        out["inputLossThresholdMsec"] = value["input_loss_threshold_msec"]
    return out


def deserialize_json(data: dict) -> InputLossFailoverSettings:
    out: InputLossFailoverSettings = {}  # type: ignore[typeddict-item]
    if "inputLossThresholdMsec" in data:
        out["input_loss_threshold_msec"] = data["inputLossThresholdMsec"]
    return out
