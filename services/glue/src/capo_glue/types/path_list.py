"""Generated from Smithy shape ``com.amazonaws.glue#PathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.path

PathList: TypeAlias = list["capo_glue.types.path.Path"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PathList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PathList:
    return list(data)
