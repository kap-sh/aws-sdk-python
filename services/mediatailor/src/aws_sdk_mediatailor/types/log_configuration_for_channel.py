"""Generated from Smithy shape ``com.amazonaws.mediatailor#LogConfigurationForChannel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.log_types


class LogConfigurationForChannel(TypedDict):
    log_types: NotRequired["aws_sdk_mediatailor.types.log_types.LogTypes"]
    """<p>The log types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogConfigurationForChannel) -> dict:
    out: dict = {}
    if "log_types" in value:
        import aws_sdk_mediatailor.types.log_types

        out["LogTypes"] = aws_sdk_mediatailor.types.log_types.serialize_json(
            value["log_types"]
        )
    return out


def deserialize_json(data: dict) -> LogConfigurationForChannel:
    out: LogConfigurationForChannel = {}  # type: ignore[typeddict-item]
    if "LogTypes" in data:
        import aws_sdk_mediatailor.types.log_types

        out["log_types"] = aws_sdk_mediatailor.types.log_types.deserialize_json(
            data["LogTypes"]
        )
    return out
