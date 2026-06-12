"""Generated from Smithy shape ``com.amazonaws.mediatailor#ConfigureLogsForChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.log_types


class ConfigureLogsForChannelResponse(TypedDict):
    channel_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the channel.</p>"""
    log_types: NotRequired["aws_sdk_mediatailor.types.log_types.LogTypes"]
    """<p>The types of logs collected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureLogsForChannelResponse) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "log_types" in value:
        import aws_sdk_mediatailor.types.log_types

        out["LogTypes"] = aws_sdk_mediatailor.types.log_types.serialize_json(
            value["log_types"]
        )
    return out


def deserialize_json(data: dict) -> ConfigureLogsForChannelResponse:
    out: ConfigureLogsForChannelResponse = {}  # type: ignore[typeddict-item]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "LogTypes" in data:
        import aws_sdk_mediatailor.types.log_types

        out["log_types"] = aws_sdk_mediatailor.types.log_types.deserialize_json(
            data["LogTypes"]
        )
    return out
