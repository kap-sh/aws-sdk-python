"""Generated from Smithy shape ``com.amazonaws.glue#StartingEventBatchCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.nullable_integer


class StartingEventBatchCondition(TypedDict, closed=True):
    batch_size: NotRequired["aws_sdk_glue.types.nullable_integer.NullableInteger"]
    """<p>Number of events in the batch.</p>"""
    batch_window: NotRequired["aws_sdk_glue.types.nullable_integer.NullableInteger"]
    """<p>Duration of the batch window in seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartingEventBatchCondition) -> dict:
    out: dict = {}
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "batch_window" in value:
        out["BatchWindow"] = value["batch_window"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartingEventBatchCondition:
    out: StartingEventBatchCondition = {}  # type: ignore[typeddict-item]
    if "BatchSize" in data:
        out["batch_size"] = data["BatchSize"]
    if "BatchWindow" in data:
        out["batch_window"] = data["BatchWindow"]
    return out
