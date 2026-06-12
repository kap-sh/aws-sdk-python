"""Generated from Smithy shape ``com.amazonaws.transfer#ProfileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

ProfileType: TypeAlias = Literal[
    "LOCAL",
    "PARTNER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOCAL",
        "PARTNER",
    )
)


def serialize_aws_json_1_1(value: ProfileType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProfileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfileType value: {data!r}")
    return cast(ProfileType, data)
