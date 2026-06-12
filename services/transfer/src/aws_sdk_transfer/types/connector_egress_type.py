"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorEgressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

ConnectorEgressType: TypeAlias = Literal[
    "SERVICE_MANAGED",
    "VPC_LATTICE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE_MANAGED",
        "VPC_LATTICE",
    )
)


def serialize_aws_json_1_1(value: ConnectorEgressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectorEgressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorEgressType value: {data!r}")
    return cast(ConnectorEgressType, data)
