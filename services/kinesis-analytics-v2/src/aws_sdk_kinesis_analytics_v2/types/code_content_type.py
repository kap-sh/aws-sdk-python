"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CodeContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

CodeContentType: TypeAlias = Literal[
    "PLAINTEXT",
    "ZIPFILE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PLAINTEXT",
        "ZIPFILE",
    )
)


def serialize_aws_json_1_1(value: CodeContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CodeContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodeContentType value: {data!r}")
    return cast(CodeContentType, data)
