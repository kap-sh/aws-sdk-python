"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MetadataModelReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class MetadataModelReference(TypedDict, closed=True):
    metadata_model_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The name of the metadata model.</p>"""
    selection_rules: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The JSON string representing metadata model location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataModelReference) -> dict:
    out: dict = {}
    if "metadata_model_name" in value:
        out["MetadataModelName"] = value["metadata_model_name"]
    if "selection_rules" in value:
        out["SelectionRules"] = value["selection_rules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetadataModelReference:
    out: MetadataModelReference = {}  # type: ignore[typeddict-item]
    if "MetadataModelName" in data:
        out["metadata_model_name"] = data["MetadataModelName"]
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    return out
