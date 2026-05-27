"""Generated from Smithy shape ``com.amazonaws.lambda#StepOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.duration_seconds


class StepOptions(TypedDict):
    next_attempt_delay_seconds: NotRequired[
        "aws_sdk_lambda.types.duration_seconds.DurationSeconds"
    ]
    """<p>The delay in seconds before the next retry attempt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepOptions) -> dict:
    out: dict = {}
    if "next_attempt_delay_seconds" in value:
        out["NextAttemptDelaySeconds"] = value["next_attempt_delay_seconds"]
    return out


def deserialize_json(data: dict) -> StepOptions:
    out: StepOptions = {}  # type: ignore[typeddict-item]
    if "NextAttemptDelaySeconds" in data:
        out["next_attempt_delay_seconds"] = data["NextAttemptDelaySeconds"]
    return out
