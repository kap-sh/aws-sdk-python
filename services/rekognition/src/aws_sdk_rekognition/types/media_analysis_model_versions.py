"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisModelVersions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.string


class MediaAnalysisModelVersions(TypedDict):
    moderation: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The Moderation base model version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisModelVersions) -> dict:
    out: dict = {}
    if "moderation" in value:
        out["Moderation"] = value["moderation"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MediaAnalysisModelVersions:
    out: MediaAnalysisModelVersions = {}  # type: ignore[typeddict-item]
    if "Moderation" in data:
        out["moderation"] = data["Moderation"]
    return out
