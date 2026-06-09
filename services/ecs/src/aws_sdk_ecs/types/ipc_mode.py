"""Generated from Smithy shape ``com.amazonaws.ecs#IpcMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

IpcMode: TypeAlias = Literal[
    "host",
    "task",
    "none",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "host",
        "task",
        "none",
    )
)


def serialize_aws_json_1_1(value: IpcMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpcMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpcMode value: {data!r}")
    return cast(IpcMode, data)
