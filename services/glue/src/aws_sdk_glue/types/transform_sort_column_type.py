"""Generated from Smithy shape ``com.amazonaws.glue#TransformSortColumnType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

TransformSortColumnType: TypeAlias = Literal[
    "NAME",
    "TRANSFORM_TYPE",
    "STATUS",
    "CREATED",
    "LAST_MODIFIED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "TRANSFORM_TYPE",
        "STATUS",
        "CREATED",
        "LAST_MODIFIED",
    )
)


def serialize_aws_json_1_1(value: TransformSortColumnType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransformSortColumnType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransformSortColumnType value: {data!r}")
    return cast(TransformSortColumnType, data)
