"""Generated from Smithy shape ``com.amazonaws.novaact#ActError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.sensitive_string


class ActError(TypedDict, closed=True):
    message: "aws_sdk_nova_act.types.sensitive_string.SensitiveString"
    """<p>A human-readable description of the error that occurred.</p>"""
    type: NotRequired["str"]
    """<p>The type or category of error that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ActError:
    out: ActError = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ActError.message required")
    if "type" in data:
        out["type"] = data["type"]
    return out
