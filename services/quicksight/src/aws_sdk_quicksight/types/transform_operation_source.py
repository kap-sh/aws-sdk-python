"""Generated from Smithy shape ``com.amazonaws.quicksight#TransformOperationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_column_id_mapping_list
    import aws_sdk_quicksight.types.data_set_entity_resource_id


class TransformOperationSource(TypedDict, closed=True):
    transform_operation_id: (
        "aws_sdk_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId"
    )
    """<p>The identifier of the transform operation that provides input data.</p>"""
    column_id_mappings: NotRequired[
        "aws_sdk_quicksight.types.data_set_column_id_mapping_list.DataSetColumnIdMappingList"
    ]
    """<p>The mappings between source column identifiers and target column identifiers for this transformation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransformOperationSource) -> dict:
    out: dict = {}
    out["TransformOperationId"] = value["transform_operation_id"]
    if "column_id_mappings" in value:
        import aws_sdk_quicksight.types.data_set_column_id_mapping_list

        out["ColumnIdMappings"] = (
            aws_sdk_quicksight.types.data_set_column_id_mapping_list.serialize_json(
                value["column_id_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransformOperationSource:
    out: TransformOperationSource = {}  # type: ignore[typeddict-item]
    if "TransformOperationId" in data:
        out["transform_operation_id"] = data["TransformOperationId"]
    else:
        raise DeserializationError(
            "TransformOperationSource.transform_operation_id required"
        )
    if "ColumnIdMappings" in data:
        import aws_sdk_quicksight.types.data_set_column_id_mapping_list

        out["column_id_mappings"] = (
            aws_sdk_quicksight.types.data_set_column_id_mapping_list.deserialize_json(
                data["ColumnIdMappings"]
            )
        )
    return out
