"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateArtifactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.artifact_properties
    import capo_sagemaker.types.artifact_source
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.metadata_properties
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.tag_list


class CreateArtifactRequest(TypedDict, closed=True):
    artifact_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the artifact. Must be unique to your account in an Amazon Web Services Region.</p>"""
    source: NotRequired["capo_sagemaker.types.artifact_source.ArtifactSource"]
    """<p>The ID, ID type, and URI of the source.</p>"""
    artifact_type: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The artifact type.</p>"""
    properties: NotRequired[
        "capo_sagemaker.types.artifact_properties.ArtifactProperties"
    ]
    """<p>A list of properties to add to the artifact.</p>"""
    metadata_properties: NotRequired[
        "capo_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags to apply to the artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateArtifactRequest) -> dict:
    out: dict = {}
    if "artifact_name" in value:
        out["ArtifactName"] = value["artifact_name"]
    if "source" in value:
        import capo_sagemaker.types.artifact_source

        out["Source"] = capo_sagemaker.types.artifact_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "artifact_type" in value:
        out["ArtifactType"] = value["artifact_type"]
    if "properties" in value:
        import capo_sagemaker.types.artifact_properties

        out["Properties"] = (
            capo_sagemaker.types.artifact_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "metadata_properties" in value:
        import capo_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            capo_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateArtifactRequest:
    out: CreateArtifactRequest = {}  # type: ignore[typeddict-item]
    if "ArtifactName" in data:
        out["artifact_name"] = data["ArtifactName"]
    if "Source" in data:
        import capo_sagemaker.types.artifact_source

        out["source"] = capo_sagemaker.types.artifact_source.deserialize_aws_json_1_1(
            data["Source"]
        )
    if "ArtifactType" in data:
        out["artifact_type"] = data["ArtifactType"]
    if "Properties" in data:
        import capo_sagemaker.types.artifact_properties

        out["properties"] = (
            capo_sagemaker.types.artifact_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "MetadataProperties" in data:
        import capo_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            capo_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
