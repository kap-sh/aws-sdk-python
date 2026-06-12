"""Generated from Smithy shape ``com.amazonaws.glue#GlueResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

GlueResourceType: TypeAlias = Literal[
    "JOB",
    "SESSION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JOB",
        "SESSION",
    )
)


def serialize_aws_json_1_1(value: GlueResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GlueResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GlueResourceType value: {data!r}")
    return cast(GlueResourceType, data)
