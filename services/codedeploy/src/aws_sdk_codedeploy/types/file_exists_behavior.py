"""Generated from Smithy shape ``com.amazonaws.codedeploy#FileExistsBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

FileExistsBehavior: TypeAlias = Literal[
    "DISALLOW",
    "OVERWRITE",
    "RETAIN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISALLOW",
        "OVERWRITE",
        "RETAIN",
    )
)


def serialize_aws_json_1_1(value: FileExistsBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileExistsBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileExistsBehavior value: {data!r}")
    return cast(FileExistsBehavior, data)
