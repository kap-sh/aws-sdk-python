"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.media_type
    import capo_sagemaker.types.trial_component_artifact_value


class TrialComponentArtifact(TypedDict, closed=True):
    media_type: NotRequired["capo_sagemaker.types.media_type.MediaType"]
    """<p>The media type of the artifact, which indicates the type of data in the artifact file. The media type consists of a <i>type</i> and a <i>subtype</i> concatenated with a slash (/) character, for example, text/csv, image/jpeg, and s3/uri. The type specifies the category of the media. The subtype specifies the kind of data.</p>"""
    value: NotRequired[
        "capo_sagemaker.types.trial_component_artifact_value.TrialComponentArtifactValue"
    ]
    """<p>The location of the artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentArtifact) -> dict:
    out: dict = {}
    if "media_type" in value:
        out["MediaType"] = value["media_type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponentArtifact:
    out: TrialComponentArtifact = {}  # type: ignore[typeddict-item]
    if "MediaType" in data:
        out["media_type"] = data["MediaType"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
