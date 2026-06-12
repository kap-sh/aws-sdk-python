"""Generated from Smithy shape ``com.amazonaws.gamelift#FilterInstanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

FilterInstanceStatus: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DRAINING",
    )
)


def serialize_aws_json_1_1(value: FilterInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterInstanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterInstanceStatus value: {data!r}")
    return cast(FilterInstanceStatus, data)
