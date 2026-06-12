"""Generated from Smithy shape ``com.amazonaws.directoryservice#SelectiveAuth``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

SelectiveAuth: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_aws_json_1_1(value: SelectiveAuth) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SelectiveAuth:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelectiveAuth value: {data!r}")
    return cast(SelectiveAuth, data)
