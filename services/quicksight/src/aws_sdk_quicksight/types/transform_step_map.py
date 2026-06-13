"""Generated from Smithy shape ``com.amazonaws.quicksight#TransformStepMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_entity_resource_id
    import aws_sdk_quicksight.types.transform_step

TransformStepMap: TypeAlias = dict[
    "aws_sdk_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId",
    "aws_sdk_quicksight.types.transform_step.TransformStep",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TransformStepMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_quicksight.types.transform_step

        out[key] = aws_sdk_quicksight.types.transform_step.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TransformStepMap:
    out: TransformStepMap = {}
    for key, value in data.items():
        import aws_sdk_quicksight.types.transform_step

        out[key] = aws_sdk_quicksight.types.transform_step.deserialize_json(value)
    return out
