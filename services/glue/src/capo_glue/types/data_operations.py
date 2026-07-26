"""Generated from Smithy shape ``com.amazonaws.glue#DataOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_operation

DataOperations: TypeAlias = list["capo_glue.types.data_operation.DataOperation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataOperations) -> list:
    import capo_glue.types.data_operation

    out: list = []
    for item in value:
        out.append(capo_glue.types.data_operation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataOperations:
    import capo_glue.types.data_operation

    out: DataOperations = []
    for item in data:
        out.append(capo_glue.types.data_operation.deserialize_aws_json_1_1(item))
    return out
