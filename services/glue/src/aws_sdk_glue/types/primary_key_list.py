"""Generated from Smithy shape ``com.amazonaws.glue#PrimaryKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.string128

PrimaryKeyList: TypeAlias = list["aws_sdk_glue.types.string128.String128"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrimaryKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PrimaryKeyList:
    return list(data)
