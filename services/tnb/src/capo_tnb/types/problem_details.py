"""Generated from Smithy shape ``com.amazonaws.tnb#ProblemDetails``."""

from typing_extensions import NotRequired, TypedDict

from capo_tnb.errors import DeserializationError


class ProblemDetails(TypedDict, closed=True):
    detail: "str"
    """<p>A human-readable explanation specific to this occurrence of the problem.</p>"""
    title: NotRequired["str"]
    """<p>A human-readable title of the problem type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProblemDetails) -> dict:
    out: dict = {}
    out["detail"] = value["detail"]
    if "title" in value:
        out["title"] = value["title"]
    return out


def deserialize_json(data: dict) -> ProblemDetails:
    out: ProblemDetails = {}  # type: ignore[typeddict-item]
    if "detail" in data:
        out["detail"] = data["detail"]
    else:
        raise DeserializationError("ProblemDetails.detail required")
    if "title" in data:
        out["title"] = data["title"]
    return out
