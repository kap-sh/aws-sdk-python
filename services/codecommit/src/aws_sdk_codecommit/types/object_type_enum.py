"""Generated from Smithy shape ``com.amazonaws.codecommit#ObjectTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

ObjectTypeEnum: TypeAlias = Literal[
    "FILE",
    "DIRECTORY",
    "GIT_LINK",
    "SYMBOLIC_LINK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FILE",
        "DIRECTORY",
        "GIT_LINK",
        "SYMBOLIC_LINK",
    )
)


def serialize_aws_json_1_1(value: ObjectTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ObjectTypeEnum value: {data!r}")
    return cast(ObjectTypeEnum, data)
