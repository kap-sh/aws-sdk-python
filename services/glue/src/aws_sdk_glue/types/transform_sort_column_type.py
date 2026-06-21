"""Generated from Smithy shape ``com.amazonaws.glue#TransformSortColumnType``."""

from typing import Literal, TypeAlias, cast

TransformSortColumnType: TypeAlias = Literal[
    "NAME",
    "TRANSFORM_TYPE",
    "STATUS",
    "CREATED",
    "LAST_MODIFIED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformSortColumnType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransformSortColumnType:
    return cast(TransformSortColumnType, data)
