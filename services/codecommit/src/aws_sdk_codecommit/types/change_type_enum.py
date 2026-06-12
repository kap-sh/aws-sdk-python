"""Generated from Smithy shape ``com.amazonaws.codecommit#ChangeTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

ChangeTypeEnum: TypeAlias = Literal[
    "A",
    "M",
    "D",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "A",
        "M",
        "D",
    )
)


def serialize_aws_json_1_1(value: ChangeTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChangeTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeTypeEnum value: {data!r}")
    return cast(ChangeTypeEnum, data)
