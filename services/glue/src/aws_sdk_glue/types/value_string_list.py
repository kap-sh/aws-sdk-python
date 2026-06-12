"""Generated from Smithy shape ``com.amazonaws.glue#ValueStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.value_string

ValueStringList: TypeAlias = list["aws_sdk_glue.types.value_string.ValueString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValueStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ValueStringList:
    return list(data)
