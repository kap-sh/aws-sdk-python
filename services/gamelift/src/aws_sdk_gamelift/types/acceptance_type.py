"""Generated from Smithy shape ``com.amazonaws.gamelift#AcceptanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

AcceptanceType: TypeAlias = Literal[
    "ACCEPT",
    "REJECT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCEPT",
        "REJECT",
    )
)


def serialize_aws_json_1_1(value: AcceptanceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceptanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceptanceType value: {data!r}")
    return cast(AcceptanceType, data)
