"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaFilesystemPermission``."""

from typing import Literal, TypeAlias, cast

LambdaFilesystemPermission: TypeAlias = Literal[
    "ro",
    "rw",
]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaFilesystemPermission) -> str:
    return value


def deserialize_json(data: str) -> LambdaFilesystemPermission:
    return cast(LambdaFilesystemPermission, data)
