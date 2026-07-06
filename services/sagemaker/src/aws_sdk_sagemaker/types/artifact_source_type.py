"""Generated from Smithy shape ``com.amazonaws.sagemaker#ArtifactSourceType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.artifact_source_id_type
    import aws_sdk_sagemaker.types.string256


class ArtifactSourceType(TypedDict, closed=True):
    source_id_type: NotRequired[
        "aws_sdk_sagemaker.types.artifact_source_id_type.ArtifactSourceIdType"
    ]
    """<p>The type of ID.</p>"""
    value: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactSourceType) -> dict:
    out: dict = {}
    if "source_id_type" in value:
        import aws_sdk_sagemaker.types.artifact_source_id_type

        out["SourceIdType"] = (
            aws_sdk_sagemaker.types.artifact_source_id_type.serialize_aws_json_1_1(
                value["source_id_type"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactSourceType:
    out: ArtifactSourceType = {}  # type: ignore[typeddict-item]
    if "SourceIdType" in data:
        import aws_sdk_sagemaker.types.artifact_source_id_type

        out["source_id_type"] = (
            aws_sdk_sagemaker.types.artifact_source_id_type.deserialize_aws_json_1_1(
                data["SourceIdType"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
