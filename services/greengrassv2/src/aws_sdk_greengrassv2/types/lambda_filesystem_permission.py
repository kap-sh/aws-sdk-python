"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaFilesystemPermission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

LambdaFilesystemPermission: TypeAlias = Literal[
    "ro",
    "rw",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ro",
        "rw",
    )
)


def serialize_json(value: LambdaFilesystemPermission) -> str:
    return value


def deserialize_json(data: str) -> LambdaFilesystemPermission:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LambdaFilesystemPermission value: {data!r}"
        )
    return cast(LambdaFilesystemPermission, data)
