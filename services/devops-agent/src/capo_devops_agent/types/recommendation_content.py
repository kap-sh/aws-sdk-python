"""Generated from Smithy shape ``com.amazonaws.devopsagent#RecommendationContent``."""

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError


class RecommendationContent(TypedDict, closed=True):
    summary: "str"
    """<p>A brief summary of the recommendation.</p>"""
    spec: NotRequired["str"]
    """<p>Agent-ready specification with detailed implementation steps</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationContent) -> dict:
    out: dict = {}
    out["summary"] = value["summary"]
    if "spec" in value:
        out["spec"] = value["spec"]
    return out


def deserialize_json(data: dict) -> RecommendationContent:
    out: RecommendationContent = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        out["summary"] = data["summary"]
    else:
        raise DeserializationError("RecommendationContent.summary required")
    if "spec" in data:
        out["spec"] = data["spec"]
    return out
