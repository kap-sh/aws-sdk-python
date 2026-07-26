"""Generated from Smithy shape ``com.amazonaws.connect#CustomerVoiceActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.timestamp


class CustomerVoiceActivity(TypedDict, closed=True):
    greeting_start_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>Timestamp that measures the beginning of the customer greeting from an outbound voice call.</p>"""
    greeting_end_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>Timestamp that measures the end of the customer greeting from an outbound voice call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerVoiceActivity) -> dict:
    out: dict = {}
    if "greeting_start_timestamp" in value:
        import capo_connect.types.timestamp

        out["GreetingStartTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["greeting_start_timestamp"]
        )
    if "greeting_end_timestamp" in value:
        import capo_connect.types.timestamp

        out["GreetingEndTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["greeting_end_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> CustomerVoiceActivity:
    out: CustomerVoiceActivity = {}  # type: ignore[typeddict-item]
    if "GreetingStartTimestamp" in data:
        import capo_connect.types.timestamp

        out["greeting_start_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["GreetingStartTimestamp"]
        )
    if "GreetingEndTimestamp" in data:
        import capo_connect.types.timestamp

        out["greeting_end_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["GreetingEndTimestamp"]
        )
    return out
