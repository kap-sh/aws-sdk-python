"""Generated from Smithy shape ``com.amazonaws.gamelift#InstanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

InstanceStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "TERMINATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACTIVE",
        "TERMINATING",
    )
)


def serialize_aws_json_1_1(value: InstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceStatus value: {data!r}")
    return cast(InstanceStatus, data)
