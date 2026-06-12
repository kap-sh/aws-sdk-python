"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeMetadataModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.metadata_model_reference_list
    import aws_sdk_database_migration_service.types.string


class DescribeMetadataModelResponse(TypedDict):
    metadata_model_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The name of the metadata model.</p>"""
    metadata_model_type: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The type of the metadata model.</p>"""
    target_metadata_models: NotRequired[
        "aws_sdk_database_migration_service.types.metadata_model_reference_list.MetadataModelReferenceList"
    ]
    """<p>A list of counterpart metadata models in the target. This field is populated only when Origin is SOURCE and after the object has been converted by DMS Schema Conversion.</p>"""
    definition: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The SQL text of the metadata model. This field might not be populated for some metadata models.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetadataModelResponse) -> dict:
    out: dict = {}
    if "metadata_model_name" in value:
        out["MetadataModelName"] = value["metadata_model_name"]
    if "metadata_model_type" in value:
        out["MetadataModelType"] = value["metadata_model_type"]
    if "target_metadata_models" in value:
        import aws_sdk_database_migration_service.types.metadata_model_reference_list

        out["TargetMetadataModels"] = (
            aws_sdk_database_migration_service.types.metadata_model_reference_list.serialize_aws_json_1_1(
                value["target_metadata_models"]
            )
        )
    if "definition" in value:
        out["Definition"] = value["definition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMetadataModelResponse:
    out: DescribeMetadataModelResponse = {}  # type: ignore[typeddict-item]
    if "MetadataModelName" in data:
        out["metadata_model_name"] = data["MetadataModelName"]
    if "MetadataModelType" in data:
        out["metadata_model_type"] = data["MetadataModelType"]
    if "TargetMetadataModels" in data:
        import aws_sdk_database_migration_service.types.metadata_model_reference_list

        out["target_metadata_models"] = (
            aws_sdk_database_migration_service.types.metadata_model_reference_list.deserialize_aws_json_1_1(
                data["TargetMetadataModels"]
            )
        )
    if "Definition" in data:
        out["definition"] = data["Definition"]
    return out
