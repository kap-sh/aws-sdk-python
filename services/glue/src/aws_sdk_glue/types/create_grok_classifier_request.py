"""Generated from Smithy shape ``com.amazonaws.glue#CreateGrokClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.classification
    import aws_sdk_glue.types.custom_patterns
    import aws_sdk_glue.types.grok_pattern
    import aws_sdk_glue.types.name_string


class CreateGrokClassifierRequest(TypedDict, closed=True):
    classification: "aws_sdk_glue.types.classification.Classification"
    """<p>An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.</p>"""
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the new classifier.</p>"""
    grok_pattern: "aws_sdk_glue.types.grok_pattern.GrokPattern"
    """<p>The grok pattern used by this classifier.</p>"""
    custom_patterns: NotRequired["aws_sdk_glue.types.custom_patterns.CustomPatterns"]
    """<p>Optional custom grok patterns used by this classifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGrokClassifierRequest) -> dict:
    out: dict = {}
    out["Classification"] = value["classification"]
    out["Name"] = value["name"]
    out["GrokPattern"] = value["grok_pattern"]
    if "custom_patterns" in value:
        out["CustomPatterns"] = value["custom_patterns"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGrokClassifierRequest:
    out: CreateGrokClassifierRequest = {}  # type: ignore[typeddict-item]
    if "Classification" in data:
        out["classification"] = data["Classification"]
    else:
        raise DeserializationError(
            "CreateGrokClassifierRequest.classification required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateGrokClassifierRequest.name required")
    if "GrokPattern" in data:
        out["grok_pattern"] = data["GrokPattern"]
    else:
        raise DeserializationError("CreateGrokClassifierRequest.grok_pattern required")
    if "CustomPatterns" in data:
        out["custom_patterns"] = data["CustomPatterns"]
    return out
