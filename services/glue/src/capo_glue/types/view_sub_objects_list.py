"""Generated from Smithy shape ``com.amazonaws.glue#ViewSubObjectsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.arn_string

ViewSubObjectsList: TypeAlias = list["capo_glue.types.arn_string.ArnString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewSubObjectsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ViewSubObjectsList:
    return list(data)
