"""Generated from Smithy shape ``com.amazonaws.glue#EventBatchingCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_size
    import aws_sdk_glue.types.batch_window


class EventBatchingCondition(TypedDict, closed=True):
    batch_size: "aws_sdk_glue.types.batch_size.BatchSize"
    """<p>Number of events that must be received from Amazon EventBridge before EventBridge event trigger fires.</p>"""
    batch_window: NotRequired["aws_sdk_glue.types.batch_window.BatchWindow"]
    """<p>Window of time in seconds after which EventBridge event trigger fires. Window starts when first event is received.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventBatchingCondition) -> dict:
    out: dict = {}
    out["BatchSize"] = value["batch_size"]
    if "batch_window" in value:
        out["BatchWindow"] = value["batch_window"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventBatchingCondition:
    out: EventBatchingCondition = {}  # type: ignore[typeddict-item]
    if "BatchSize" in data:
        out["batch_size"] = data["BatchSize"]
    else:
        raise DeserializationError("EventBatchingCondition.batch_size required")
    if "BatchWindow" in data:
        out["batch_window"] = data["BatchWindow"]
    return out
