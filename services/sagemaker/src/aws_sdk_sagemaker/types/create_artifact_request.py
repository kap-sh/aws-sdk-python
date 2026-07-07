"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateArtifactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.artifact_properties
    import aws_sdk_sagemaker.types.artifact_source
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.metadata_properties
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.tag_list


class CreateArtifactRequest(TypedDict, closed=True):
    artifact_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the artifact. Must be unique to your account in an Amazon Web Services Region.</p>"""
    source: NotRequired["aws_sdk_sagemaker.types.artifact_source.ArtifactSource"]
    """<p>The ID, ID type, and URI of the source.</p>"""
    artifact_type: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The artifact type.</p>"""
    properties: NotRequired[
        "aws_sdk_sagemaker.types.artifact_properties.ArtifactProperties"
    ]
    """<p>A list of properties to add to the artifact.</p>"""
    metadata_properties: NotRequired[
        "aws_sdk_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags to apply to the artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateArtifactRequest) -> dict:
    out: dict = {}
    if "artifact_name" in value:
        out["ArtifactName"] = value["artifact_name"]
    if "source" in value:
        import aws_sdk_sagemaker.types.artifact_source

        out["Source"] = aws_sdk_sagemaker.types.artifact_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "artifact_type" in value:
        out["ArtifactType"] = value["artifact_type"]
    if "properties" in value:
        import aws_sdk_sagemaker.types.artifact_properties

        out["Properties"] = (
            aws_sdk_sagemaker.types.artifact_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "metadata_properties" in value:
        import aws_sdk_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            aws_sdk_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateArtifactRequest:
    out: CreateArtifactRequest = {}  # type: ignore[typeddict-item]
    if "ArtifactName" in data:
        out["artifact_name"] = data["ArtifactName"]
    if "Source" in data:
        import aws_sdk_sagemaker.types.artifact_source

        out["source"] = (
            aws_sdk_sagemaker.types.artifact_source.deserialize_aws_json_1_1(
                data["Source"]
            )
        )
    if "ArtifactType" in data:
        out["artifact_type"] = data["ArtifactType"]
    if "Properties" in data:
        import aws_sdk_sagemaker.types.artifact_properties

        out["properties"] = (
            aws_sdk_sagemaker.types.artifact_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "MetadataProperties" in data:
        import aws_sdk_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            aws_sdk_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
