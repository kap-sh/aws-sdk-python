"""Generated from Smithy shape ``com.amazonaws.codecommit#ConflictDetailLevelTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

ConflictDetailLevelTypeEnum: TypeAlias = Literal[
    "FILE_LEVEL",
    "LINE_LEVEL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FILE_LEVEL",
        "LINE_LEVEL",
    )
)


def serialize_aws_json_1_1(value: ConflictDetailLevelTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConflictDetailLevelTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConflictDetailLevelTypeEnum value: {data!r}"
        )
    return cast(ConflictDetailLevelTypeEnum, data)
