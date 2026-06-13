"""Generated from Smithy shape ``com.amazonaws.quicksight#DestinationTableSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_entity_resource_id


class DestinationTableSource(TypedDict):
    transform_operation_id: (
        "aws_sdk_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId"
    )
    """<p>The identifier of the transform operation that provides data to the destination table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationTableSource) -> dict:
    out: dict = {}
    out["TransformOperationId"] = value["transform_operation_id"]
    return out


def deserialize_json(data: dict) -> DestinationTableSource:
    out: DestinationTableSource = {}  # type: ignore[typeddict-item]
    if "TransformOperationId" in data:
        out["transform_operation_id"] = data["TransformOperationId"]
    else:
        raise DeserializationError(
            "DestinationTableSource.transform_operation_id required"
        )
    return out
