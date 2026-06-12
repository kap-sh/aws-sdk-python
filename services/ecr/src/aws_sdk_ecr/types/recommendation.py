"""Generated from Smithy shape ``com.amazonaws.ecr#Recommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.recommendation_text
    import aws_sdk_ecr.types.url


class Recommendation(TypedDict):
    url: NotRequired["aws_sdk_ecr.types.url.Url"]
    """<p>The URL address to the CVE remediation recommendations.</p>"""
    text: NotRequired["aws_sdk_ecr.types.recommendation_text.RecommendationText"]
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
    if "url" in data:
        out["url"] = data["url"]
    if "text" in data:
        out["text"] = data["text"]
    return out
