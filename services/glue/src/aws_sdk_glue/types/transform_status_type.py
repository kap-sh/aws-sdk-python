"""Generated from Smithy shape ``com.amazonaws.glue#TransformStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

TransformStatusType: TypeAlias = Literal[
    "NOT_READY",
    "READY",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_READY",
        "READY",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: TransformStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransformStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransformStatusType value: {data!r}")
    return cast(TransformStatusType, data)
