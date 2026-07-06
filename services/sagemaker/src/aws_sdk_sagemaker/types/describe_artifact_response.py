"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeArtifactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.artifact_arn
    import aws_sdk_sagemaker.types.artifact_source
    import aws_sdk_sagemaker.types.experiment_entity_name_or_arn
    import aws_sdk_sagemaker.types.lineage_entity_parameters
    import aws_sdk_sagemaker.types.lineage_group_arn
    import aws_sdk_sagemaker.types.metadata_properties
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.user_context


class DescribeArtifactResponse(TypedDict, closed=True):
    artifact_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name_or_arn.ExperimentEntityNameOrArn"
    ]
    """<p>The name of the artifact.</p>"""
    artifact_arn: NotRequired["aws_sdk_sagemaker.types.artifact_arn.ArtifactArn"]
    """<p>The Amazon Resource Name (ARN) of the artifact.</p>"""
    source: NotRequired["aws_sdk_sagemaker.types.artifact_source.ArtifactSource"]
    """<p>The source of the artifact.</p>"""
    artifact_type: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The type of the artifact.</p>"""
    properties: NotRequired[
        "aws_sdk_sagemaker.types.lineage_entity_parameters.LineageEntityParameters"
    ]
    """<p>A list of the artifact's properties.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the artifact was created.</p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the artifact was last modified.</p>"""
    last_modified_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    metadata_properties: NotRequired[
        "aws_sdk_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    lineage_group_arn: NotRequired[
        "aws_sdk_sagemaker.types.lineage_group_arn.LineageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lineage group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeArtifactResponse) -> dict:
    out: dict = {}
    if "artifact_name" in value:
        out["ArtifactName"] = value["artifact_name"]
    if "artifact_arn" in value:
        out["ArtifactArn"] = value["artifact_arn"]
    if "source" in value:
        import aws_sdk_sagemaker.types.artifact_source

        out["Source"] = aws_sdk_sagemaker.types.artifact_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "artifact_type" in value:
        out["ArtifactType"] = value["artifact_type"]
    if "properties" in value:
        import aws_sdk_sagemaker.types.lineage_entity_parameters

        out["Properties"] = (
            aws_sdk_sagemaker.types.lineage_entity_parameters.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["CreatedBy"] = aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_modified_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "metadata_properties" in value:
        import aws_sdk_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            aws_sdk_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "lineage_group_arn" in value:
        out["LineageGroupArn"] = value["lineage_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeArtifactResponse:
    out: DescribeArtifactResponse = {}  # type: ignore[typeddict-item]
    if "ArtifactName" in data:
        out["artifact_name"] = data["ArtifactName"]
    if "ArtifactArn" in data:
        out["artifact_arn"] = data["ArtifactArn"]
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
        import aws_sdk_sagemaker.types.lineage_entity_parameters

        out["properties"] = (
            aws_sdk_sagemaker.types.lineage_entity_parameters.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CreatedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["created_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["CreatedBy"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["last_modified_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "MetadataProperties" in data:
        import aws_sdk_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            aws_sdk_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if "LineageGroupArn" in data:
        out["lineage_group_arn"] = data["LineageGroupArn"]
    return out
