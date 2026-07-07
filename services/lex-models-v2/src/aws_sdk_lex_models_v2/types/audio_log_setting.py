"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AudioLogSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.audio_log_destination
    import aws_sdk_lex_models_v2.types.boolean
    import aws_sdk_lex_models_v2.types.boxed_boolean


class AudioLogSetting(TypedDict, closed=True):
    enabled: "aws_sdk_lex_models_v2.types.boolean.Boolean"
    """<p>Determines whether audio logging in enabled for the bot.</p>"""
    destination: "aws_sdk_lex_models_v2.types.audio_log_destination.AudioLogDestination"
    selective_logging_enabled: NotRequired[
        "aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>The option to enable selective conversation log capture for audio.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioLogSetting) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    import aws_sdk_lex_models_v2.types.audio_log_destination

    out["destination"] = (
        aws_sdk_lex_models_v2.types.audio_log_destination.serialize_json(
            value["destination"]
        )
    )
    if "selective_logging_enabled" in value:
        out["selectiveLoggingEnabled"] = value["selective_logging_enabled"]
    return out


def deserialize_json(data: dict) -> AudioLogSetting:
    out: AudioLogSetting = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "destination" in data:
        import aws_sdk_lex_models_v2.types.audio_log_destination

        out["destination"] = (
            aws_sdk_lex_models_v2.types.audio_log_destination.deserialize_json(
                data["destination"]
            )
        )
    else:
        raise DeserializationError("AudioLogSetting.destination required")
    if "selectiveLoggingEnabled" in data:
        out["selective_logging_enabled"] = data["selectiveLoggingEnabled"]
    return out
