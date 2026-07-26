"""Generated from Smithy shape ``com.amazonaws.mediatailor#ConfigureLogsForChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.log_types


class ConfigureLogsForChannelResponse(TypedDict, closed=True):
    channel_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name of the channel.</p>"""
    log_types: NotRequired["capo_mediatailor.types.log_types.LogTypes"]
    """<p>The types of logs collected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureLogsForChannelResponse) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "log_types" in value:
        import capo_mediatailor.types.log_types

        out["LogTypes"] = capo_mediatailor.types.log_types.serialize_json(
            value["log_types"]
        )
    return out


def deserialize_json(data: dict) -> ConfigureLogsForChannelResponse:
    out: ConfigureLogsForChannelResponse = {}  # type: ignore[typeddict-item]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "LogTypes" in data:
        import capo_mediatailor.types.log_types

        out["log_types"] = capo_mediatailor.types.log_types.deserialize_json(
            data["LogTypes"]
        )
    return out
