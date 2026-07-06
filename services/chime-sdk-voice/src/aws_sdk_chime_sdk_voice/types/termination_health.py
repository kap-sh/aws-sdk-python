"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#TerminationHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.iso8601_timestamp
    import aws_sdk_chime_sdk_voice.types.string


class TerminationHealth(TypedDict, closed=True):
    timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The timestamp, in ISO 8601 format.</p>"""
    source: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The source IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminationHealth) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["Timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["timestamp"]
            )
        )
    if "source" in value:
        out["Source"] = value["source"]
    return out


def deserialize_json(data: dict) -> TerminationHealth:
    out: TerminationHealth = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["Timestamp"]
            )
        )
    if "Source" in data:
        out["source"] = data["Source"]
    return out
