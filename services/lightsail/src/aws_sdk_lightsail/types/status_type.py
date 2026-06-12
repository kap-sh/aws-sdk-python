"""Generated from Smithy shape ``com.amazonaws.lightsail#StatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

StatusType: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
    )
)


def serialize_aws_json_1_1(value: StatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusType value: {data!r}")
    return cast(StatusType, data)
