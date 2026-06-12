"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

AppBlockState: TypeAlias = Literal[
    "INACTIVE",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INACTIVE",
        "ACTIVE",
    )
)


def serialize_aws_json_1_1(value: AppBlockState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppBlockState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppBlockState value: {data!r}")
    return cast(AppBlockState, data)
