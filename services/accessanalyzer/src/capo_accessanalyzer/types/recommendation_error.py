"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RecommendationError``."""

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError


class RecommendationError(TypedDict, closed=True):
    code: "str"
    """<p>The error code for a failed retrieval of a recommendation for a finding.</p>"""
    message: "str"
    """<p>The error message for a failed retrieval of a recommendation for a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationError) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RecommendationError:
    out: RecommendationError = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("RecommendationError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("RecommendationError.message required")
    return out
