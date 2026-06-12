"""Generated from Smithy shape ``com.amazonaws.glue#NullValueFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.null_value_field

NullValueFields: TypeAlias = list["aws_sdk_glue.types.null_value_field.NullValueField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NullValueFields) -> list:
    import aws_sdk_glue.types.null_value_field

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.null_value_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NullValueFields:
    import aws_sdk_glue.types.null_value_field

    out: NullValueFields = []
    for item in data:
        out.append(aws_sdk_glue.types.null_value_field.deserialize_aws_json_1_1(item))
    return out
