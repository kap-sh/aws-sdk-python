"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateValidationStatusReason``."""

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError


class AnalysisTemplateValidationStatusReason(TypedDict, closed=True):
    message: "str"
    """<p>The validation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateValidationStatusReason) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AnalysisTemplateValidationStatusReason:
    out: AnalysisTemplateValidationStatusReason = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "AnalysisTemplateValidationStatusReason.message required"
        )
    return out
