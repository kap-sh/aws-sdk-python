"""Generated from Smithy shape ``com.amazonaws.codecommit#ReplacementTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

ReplacementTypeEnum: TypeAlias = Literal[
    "KEEP_BASE",
    "KEEP_SOURCE",
    "KEEP_DESTINATION",
    "USE_NEW_CONTENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KEEP_BASE",
        "KEEP_SOURCE",
        "KEEP_DESTINATION",
        "USE_NEW_CONTENT",
    )
)


def serialize_aws_json_1_1(value: ReplacementTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplacementTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplacementTypeEnum value: {data!r}")
    return cast(ReplacementTypeEnum, data)
