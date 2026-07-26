"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TextLogSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boolean
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.text_log_destination


class TextLogSetting(TypedDict, closed=True):
    enabled: "capo_lex_models_v2.types.boolean.Boolean"
    """<p>Determines whether conversation logs should be stored for an alias.</p>"""
    destination: "capo_lex_models_v2.types.text_log_destination.TextLogDestination"
    selective_logging_enabled: NotRequired[
        "capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>The option to enable selective conversation log capture for text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextLogSetting) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    import capo_lex_models_v2.types.text_log_destination

    out["destination"] = capo_lex_models_v2.types.text_log_destination.serialize_json(
        value["destination"]
    )
    if "selective_logging_enabled" in value:
        out["selectiveLoggingEnabled"] = value["selective_logging_enabled"]
    return out


def deserialize_json(data: dict) -> TextLogSetting:
    out: TextLogSetting = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "destination" in data:
        import capo_lex_models_v2.types.text_log_destination

        out["destination"] = (
            capo_lex_models_v2.types.text_log_destination.deserialize_json(
                data["destination"]
            )
        )
    else:
        raise DeserializationError("TextLogSetting.destination required")
    if "selectiveLoggingEnabled" in data:
        out["selective_logging_enabled"] = data["selectiveLoggingEnabled"]
    return out
