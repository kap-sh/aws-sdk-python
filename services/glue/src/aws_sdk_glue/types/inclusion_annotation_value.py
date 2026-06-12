"""Generated from Smithy shape ``com.amazonaws.glue#InclusionAnnotationValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

InclusionAnnotationValue: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_aws_json_1_1(value: InclusionAnnotationValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InclusionAnnotationValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InclusionAnnotationValue value: {data!r}")
    return cast(InclusionAnnotationValue, data)
