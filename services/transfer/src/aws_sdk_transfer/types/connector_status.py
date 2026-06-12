"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

ConnectorStatus: TypeAlias = Literal[
    "ACTIVE",
    "ERRORED",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ERRORED",
        "PENDING",
    )
)


def serialize_aws_json_1_1(value: ConnectorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorStatus value: {data!r}")
    return cast(ConnectorStatus, data)
