"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisDetectModerationLabelsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.project_version_id


class MediaAnalysisDetectModerationLabelsConfig(TypedDict, closed=True):
    min_confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Specifies the minimum confidence level for the moderation labels to return. Amazon Rekognition doesn't return any labels with a confidence level lower than this specified value. </p>"""
    project_version: NotRequired[
        "aws_sdk_rekognition.types.project_version_id.ProjectVersionId"
    ]
    """<p>Specifies the custom moderation model to be used during the label detection job. If not provided the pre-trained model is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisDetectModerationLabelsConfig) -> dict:
    out: dict = {}
    if "min_confidence" in value:
        out["MinConfidence"] = value["min_confidence"]
    if "project_version" in value:
        out["ProjectVersion"] = value["project_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MediaAnalysisDetectModerationLabelsConfig:
    out: MediaAnalysisDetectModerationLabelsConfig = {}  # type: ignore[typeddict-item]
    if "MinConfidence" in data:
        out["min_confidence"] = data["MinConfidence"]
    if "ProjectVersion" in data:
        out["project_version"] = data["ProjectVersion"]
    return out
