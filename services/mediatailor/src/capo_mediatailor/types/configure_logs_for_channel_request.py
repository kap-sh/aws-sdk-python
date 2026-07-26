"""Generated from Smithy shape ``com.amazonaws.mediatailor#ConfigureLogsForChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.log_types


class ConfigureLogsForChannelRequest(TypedDict, closed=True):
    channel_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the channel.</p>"""
    log_types: "capo_mediatailor.types.log_types.LogTypes"
    """<p>The types of logs to collect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureLogsForChannelRequest) -> dict:
    out: dict = {}
    out["ChannelName"] = value["channel_name"]
    import capo_mediatailor.types.log_types

    out["LogTypes"] = capo_mediatailor.types.log_types.serialize_json(
        value["log_types"]
    )
    return out


def deserialize_json(data: dict) -> ConfigureLogsForChannelRequest:
    out: ConfigureLogsForChannelRequest = {}  # type: ignore[typeddict-item]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError(
            "ConfigureLogsForChannelRequest.channel_name required"
        )
    if "LogTypes" in data:
        import capo_mediatailor.types.log_types

        out["log_types"] = capo_mediatailor.types.log_types.deserialize_json(
            data["LogTypes"]
        )
    else:
        raise DeserializationError("ConfigureLogsForChannelRequest.log_types required")
    return out
