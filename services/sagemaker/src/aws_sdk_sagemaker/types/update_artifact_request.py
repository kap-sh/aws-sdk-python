"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateArtifactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.artifact_arn
    import aws_sdk_sagemaker.types.artifact_properties
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.list_lineage_entity_parameter_key


class UpdateArtifactRequest(TypedDict):
    artifact_arn: NotRequired["aws_sdk_sagemaker.types.artifact_arn.ArtifactArn"]
    """<p>The Amazon Resource Name (ARN) of the artifact to update.</p>"""
    artifact_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The new name for the artifact.</p>"""
    properties: NotRequired[
        "aws_sdk_sagemaker.types.artifact_properties.ArtifactProperties"
    ]
    """<p>The new list of properties. Overwrites the current property list.</p>"""
    properties_to_remove: NotRequired[
        "aws_sdk_sagemaker.types.list_lineage_entity_parameter_key.ListLineageEntityParameterKey"
    ]
    """<p>A list of properties to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateArtifactRequest) -> dict:
    out: dict = {}
    if "artifact_arn" in value:
        out["ArtifactArn"] = value["artifact_arn"]
    if "artifact_name" in value:
        out["ArtifactName"] = value["artifact_name"]
    if "properties" in value:
        import aws_sdk_sagemaker.types.artifact_properties

        out["Properties"] = (
            aws_sdk_sagemaker.types.artifact_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "properties_to_remove" in value:
        import aws_sdk_sagemaker.types.list_lineage_entity_parameter_key

        out["PropertiesToRemove"] = (
            aws_sdk_sagemaker.types.list_lineage_entity_parameter_key.serialize_aws_json_1_1(
                value["properties_to_remove"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateArtifactRequest:
    out: UpdateArtifactRequest = {}  # type: ignore[typeddict-item]
    if "ArtifactArn" in data:
        out["artifact_arn"] = data["ArtifactArn"]
    if "ArtifactName" in data:
        out["artifact_name"] = data["ArtifactName"]
    if "Properties" in data:
        import aws_sdk_sagemaker.types.artifact_properties

        out["properties"] = (
            aws_sdk_sagemaker.types.artifact_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "PropertiesToRemove" in data:
        import aws_sdk_sagemaker.types.list_lineage_entity_parameter_key

        out["properties_to_remove"] = (
            aws_sdk_sagemaker.types.list_lineage_entity_parameter_key.deserialize_aws_json_1_1(
                data["PropertiesToRemove"]
            )
        )
    return out
