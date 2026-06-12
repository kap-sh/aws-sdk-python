"""Generated from Smithy shape ``com.amazonaws.glue#ContextWords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string

ContextWords: TypeAlias = list["aws_sdk_glue.types.name_string.NameString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContextWords) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ContextWords:
    return list(data)
