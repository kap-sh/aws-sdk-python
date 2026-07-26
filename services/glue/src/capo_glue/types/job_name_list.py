"""Generated from Smithy shape ``com.amazonaws.glue#JobNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.name_string

JobNameList: TypeAlias = list["capo_glue.types.name_string.NameString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> JobNameList:
    return list(data)
