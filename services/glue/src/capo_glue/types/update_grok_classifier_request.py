"""Generated from Smithy shape ``com.amazonaws.glue#UpdateGrokClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.classification
    import capo_glue.types.custom_patterns
    import capo_glue.types.grok_pattern
    import capo_glue.types.name_string


class UpdateGrokClassifierRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the <code>GrokClassifier</code>.</p>"""
    classification: NotRequired["capo_glue.types.classification.Classification"]
    """<p>An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.</p>"""
    grok_pattern: NotRequired["capo_glue.types.grok_pattern.GrokPattern"]
    """<p>The grok pattern used by this classifier.</p>"""
    custom_patterns: NotRequired["capo_glue.types.custom_patterns.CustomPatterns"]
    """<p>Optional custom grok patterns used by this classifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGrokClassifierRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "grok_pattern" in value:
        out["GrokPattern"] = value["grok_pattern"]
    if "custom_patterns" in value:
        out["CustomPatterns"] = value["custom_patterns"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGrokClassifierRequest:
    out: UpdateGrokClassifierRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateGrokClassifierRequest.name required")
    if "Classification" in data:
        out["classification"] = data["Classification"]
    if "GrokPattern" in data:
        out["grok_pattern"] = data["GrokPattern"]
    if "CustomPatterns" in data:
        out["custom_patterns"] = data["CustomPatterns"]
    return out
