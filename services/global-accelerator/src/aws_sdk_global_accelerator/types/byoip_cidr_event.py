"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ByoipCidrEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string
    import aws_sdk_global_accelerator.types.timestamp


class ByoipCidrEvent(TypedDict):
    message: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>A string that contains an <code>Event</code> message describing changes that you make in the status of an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).</p>"""
    timestamp: NotRequired["aws_sdk_global_accelerator.types.timestamp.Timestamp"]
    """<p>A timestamp for when you make a status change for an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByoipCidrEvent) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "timestamp" in value:
        import aws_sdk_global_accelerator.types.timestamp

        out["Timestamp"] = (
            aws_sdk_global_accelerator.types.timestamp.serialize_aws_json_1_1(
                value["timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ByoipCidrEvent:
    out: ByoipCidrEvent = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Timestamp" in data:
        import aws_sdk_global_accelerator.types.timestamp

        out["timestamp"] = (
            aws_sdk_global_accelerator.types.timestamp.deserialize_aws_json_1_1(
                data["Timestamp"]
            )
        )
    return out
