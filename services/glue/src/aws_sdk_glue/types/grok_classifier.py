"""Generated from Smithy shape ``com.amazonaws.glue#GrokClassifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.classification
    import aws_sdk_glue.types.custom_patterns
    import aws_sdk_glue.types.grok_pattern
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.version_id


class GrokClassifier(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    classification: "aws_sdk_glue.types.classification.Classification"
    """<p>An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, and so on.</p>"""
    creation_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time that this classifier was registered.</p>"""
    last_updated: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time that this classifier was last updated.</p>"""
    version: "aws_sdk_glue.types.version_id.VersionId"
    """<p>The version of this classifier.</p>"""
    grok_pattern: "aws_sdk_glue.types.grok_pattern.GrokPattern"
    r"""<p>The grok pattern applied to a data store by this classifier. For more information, see built-in patterns in <a href=\"https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html\">Writing Custom Classifiers</a>.</p>"""
    custom_patterns: NotRequired["aws_sdk_glue.types.custom_patterns.CustomPatterns"]
    r"""<p>Optional custom grok patterns defined by this classifier. For more information, see custom patterns in <a href=\"https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html\">Writing Custom Classifiers</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrokClassifier) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Classification"] = value["classification"]
    if "creation_time" in value:
        import aws_sdk_glue.types.timestamp

        out["CreationTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_updated" in value:
        import aws_sdk_glue.types.timestamp

        out["LastUpdated"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_updated"]
        )
    out["Version"] = value.get("version", 0)
    out["GrokPattern"] = value["grok_pattern"]
    if "custom_patterns" in value:
        out["CustomPatterns"] = value["custom_patterns"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GrokClassifier:
    out: GrokClassifier = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GrokClassifier.name required")
    if "Classification" in data:
        out["classification"] = data["Classification"]
    else:
        raise DeserializationError("GrokClassifier.classification required")
    if "CreationTime" in data:
        import aws_sdk_glue.types.timestamp

        out["creation_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastUpdated" in data:
        import aws_sdk_glue.types.timestamp

        out["last_updated"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastUpdated"]
        )
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if "GrokPattern" in data:
        out["grok_pattern"] = data["GrokPattern"]
    else:
        raise DeserializationError("GrokClassifier.grok_pattern required")
    if "CustomPatterns" in data:
        out["custom_patterns"] = data["CustomPatterns"]
    return out
