"""Generated from Smithy shape ``com.amazonaws.workspaces#ModificationStateEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

ModificationStateEnum: TypeAlias = Literal[
    "UPDATE_INITIATED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATE_INITIATED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_FAILED",
    )
)


def serialize_aws_json_1_1(value: ModificationStateEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModificationStateEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModificationStateEnum value: {data!r}")
    return cast(ModificationStateEnum, data)
