"""Generated from Smithy shape ``com.amazonaws.glue#FieldsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.field

FieldsList: TypeAlias = list["aws_sdk_glue.types.field.Field"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldsList) -> list:
    import aws_sdk_glue.types.field

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FieldsList:
    import aws_sdk_glue.types.field

    out: FieldsList = []
    for item in data:
        out.append(aws_sdk_glue.types.field.deserialize_aws_json_1_1(item))
    return out
