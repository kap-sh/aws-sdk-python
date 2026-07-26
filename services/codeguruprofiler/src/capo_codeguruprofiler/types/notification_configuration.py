"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#NotificationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.channels


class NotificationConfiguration(TypedDict, closed=True):
    channels: NotRequired["capo_codeguruprofiler.types.channels.Channels"]
    """<p>List of up to two channels to be used for sending notifications for events detected from the application profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfiguration) -> dict:
    out: dict = {}
    if "channels" in value:
        import capo_codeguruprofiler.types.channels

        out["channels"] = capo_codeguruprofiler.types.channels.serialize_json(
            value["channels"]
        )
    return out


def deserialize_json(data: dict) -> NotificationConfiguration:
    out: NotificationConfiguration = {}  # type: ignore[typeddict-item]
    if "channels" in data:
        import capo_codeguruprofiler.types.channels

        out["channels"] = capo_codeguruprofiler.types.channels.deserialize_json(
            data["channels"]
        )
    return out
