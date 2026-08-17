"""Generated from Smithy shape ``com.amazonaws.ecr#Recommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.recommendation_text
    import capo_ecr.types.url


class Recommendation(TypedDict, closed=True):
    url: NotRequired["capo_ecr.types.url.Url"]
    """<p>The URL address to the CVE remediation recommendations.</p>"""
    text: NotRequired["capo_ecr.types.recommendation_text.RecommendationText"]
    """<p>The recommended course of action to remediate the finding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Recommendation) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out
