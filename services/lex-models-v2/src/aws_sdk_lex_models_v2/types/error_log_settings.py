"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ErrorLogSettings``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boxed_boolean


class ErrorLogSettings(TypedDict):
    enabled: "aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Settings parameters for the error logs, when it is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorLogSettings) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> ErrorLogSettings:
    out: ErrorLogSettings = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        raise DeserializationError("ErrorLogSettings.enabled required")
    return out
