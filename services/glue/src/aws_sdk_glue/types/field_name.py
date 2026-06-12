"""Generated from Smithy shape ``com.amazonaws.glue#FieldName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

FieldName: TypeAlias = Literal[
    "CRAWL_ID",
    "STATE",
    "START_TIME",
    "END_TIME",
    "DPU_HOUR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRAWL_ID",
        "STATE",
        "START_TIME",
        "END_TIME",
        "DPU_HOUR",
    )
)


def serialize_aws_json_1_1(value: FieldName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FieldName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FieldName value: {data!r}")
    return cast(FieldName, data)
