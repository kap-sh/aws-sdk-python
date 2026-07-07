"""Generated from Smithy shape ``com.amazonaws.rekognition#ModerationLabel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.string
    import aws_sdk_rekognition.types.u_integer


class ModerationLabel(TypedDict, closed=True):
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Specifies the confidence that Amazon Rekognition has that the label has been correctly identified.</p> <p>If you don't specify the <code>MinConfidence</code> parameter in the call to <code>DetectModerationLabels</code>, the operation returns labels with a confidence value greater than or equal to 50 percent.</p>"""
    name: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The label name for the type of unsafe content detected in the image.</p>"""
    parent_name: NotRequired["aws_sdk_rekognition.types.string.String"]
    r"""<p>The name for the parent label. Labels at the top level of the hierarchy have the parent label <code>\"\"</code>.</p>"""
    taxonomy_level: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p>The level of the moderation label with regard to its taxonomy, from 1 to 3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModerationLabel) -> dict:
    out: dict = {}
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "name" in value:
        out["Name"] = value["name"]
    if "parent_name" in value:
        out["ParentName"] = value["parent_name"]
    if "taxonomy_level" in value:
        out["TaxonomyLevel"] = value["taxonomy_level"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModerationLabel:
    out: ModerationLabel = {}  # type: ignore[typeddict-item]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ParentName" in data:
        out["parent_name"] = data["ParentName"]
    if "TaxonomyLevel" in data:
        out["taxonomy_level"] = data["TaxonomyLevel"]
    return out
