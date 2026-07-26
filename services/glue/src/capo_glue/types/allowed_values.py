"""Generated from Smithy shape ``com.amazonaws.glue#AllowedValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.allowed_value

AllowedValues: TypeAlias = list["capo_glue.types.allowed_value.AllowedValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedValues) -> list:
    import capo_glue.types.allowed_value

    out: list = []
    for item in value:
        out.append(capo_glue.types.allowed_value.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AllowedValues:
    import capo_glue.types.allowed_value

    out: AllowedValues = []
    for item in data:
        out.append(capo_glue.types.allowed_value.deserialize_aws_json_1_1(item))
    return out
