"""Generated from Smithy shape ``com.amazonaws.ssm#ManagedStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ManagedStatus: TypeAlias = Literal[
    "All",
    "Managed",
    "Unmanaged",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "All",
        "Managed",
        "Unmanaged",
    )
)


def serialize_aws_json_1_1(value: ManagedStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagedStatus value: {data!r}")
    return cast(ManagedStatus, data)
