"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanReasoningValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_sensitive_string


class SpanReasoningValue(TypedDict, closed=True):
    value: "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    """<p>The reasoning text content</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanReasoningValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SpanReasoningValue:
    out: SpanReasoningValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SpanReasoningValue.value required")
    return out
