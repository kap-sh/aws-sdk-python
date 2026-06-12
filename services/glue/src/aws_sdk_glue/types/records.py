"""Generated from Smithy shape ``com.amazonaws.glue#Records``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.record

Records: TypeAlias = list["aws_sdk_glue.types.record.Record"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Records) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Records:
    return list(data)
