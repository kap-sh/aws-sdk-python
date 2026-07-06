"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetCustomEntityTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.custom_entity_type_names
    import aws_sdk_glue.types.custom_entity_types


class BatchGetCustomEntityTypesResponse(TypedDict, closed=True):
    custom_entity_types: NotRequired[
        "aws_sdk_glue.types.custom_entity_types.CustomEntityTypes"
    ]
    """<p>A list of <code>CustomEntityType</code> objects representing the custom patterns that have been created.</p>"""
    custom_entity_types_not_found: NotRequired[
        "aws_sdk_glue.types.custom_entity_type_names.CustomEntityTypeNames"
    ]
    """<p>A list of the names of custom patterns that were not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCustomEntityTypesResponse) -> dict:
    out: dict = {}
    if "custom_entity_types" in value:
        import aws_sdk_glue.types.custom_entity_types

        out["CustomEntityTypes"] = (
            aws_sdk_glue.types.custom_entity_types.serialize_aws_json_1_1(
                value["custom_entity_types"]
            )
        )
    if "custom_entity_types_not_found" in value:
        import aws_sdk_glue.types.custom_entity_type_names

        out["CustomEntityTypesNotFound"] = (
            aws_sdk_glue.types.custom_entity_type_names.serialize_aws_json_1_1(
                value["custom_entity_types_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCustomEntityTypesResponse:
    out: BatchGetCustomEntityTypesResponse = {}  # type: ignore[typeddict-item]
    if "CustomEntityTypes" in data:
        import aws_sdk_glue.types.custom_entity_types

        out["custom_entity_types"] = (
            aws_sdk_glue.types.custom_entity_types.deserialize_aws_json_1_1(
                data["CustomEntityTypes"]
            )
        )
    if "CustomEntityTypesNotFound" in data:
        import aws_sdk_glue.types.custom_entity_type_names

        out["custom_entity_types_not_found"] = (
            aws_sdk_glue.types.custom_entity_type_names.deserialize_aws_json_1_1(
                data["CustomEntityTypesNotFound"]
            )
        )
    return out
