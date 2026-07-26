"""Generated from Smithy shape ``com.amazonaws.glue#DeleteConnectionNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.name_string

DeleteConnectionNameList: TypeAlias = list["capo_glue.types.name_string.NameString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConnectionNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeleteConnectionNameList:
    return list(data)
