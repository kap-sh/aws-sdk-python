"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AcceleratorEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.timestamp


class AcceleratorEvent(TypedDict, closed=True):
    message: NotRequired["capo_global_accelerator.types.generic_string.GenericString"]
    """<p>A string that contains an <code>Event</code> message describing changes or errors when you update an accelerator in Global Accelerator from IPv4 to dual-stack, or dual-stack to IPv4.</p>"""
    timestamp: NotRequired["capo_global_accelerator.types.timestamp.Timestamp"]
    """<p>A timestamp for when you update an accelerator in Global Accelerator from IPv4 to dual-stack, or dual-stack to IPv4.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorEvent) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "timestamp" in value:
        import capo_global_accelerator.types.timestamp

        out["Timestamp"] = (
            capo_global_accelerator.types.timestamp.serialize_aws_json_1_1(
                value["timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceleratorEvent:
    out: AcceleratorEvent = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Timestamp" in data:
        import capo_global_accelerator.types.timestamp

        out["timestamp"] = (
            capo_global_accelerator.types.timestamp.deserialize_aws_json_1_1(
                data["Timestamp"]
            )
        )
    return out
