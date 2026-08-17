"""Generated from Smithy shape ``com.amazonaws.scheduler#DeadLetterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.resource_arn


class DeadLetterConfig(TypedDict, closed=True):
    arn: NotRequired["capo_scheduler.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the SQS queue specified as the destination for the dead-letter queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeadLetterConfig) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeadLetterConfig:
    out: DeadLetterConfig = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
