"""Generated from Smithy shape ``com.amazonaws.fms#TargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

TargetType: TypeAlias = Literal[
    "GATEWAY",
    "CARRIER_GATEWAY",
    "INSTANCE",
    "LOCAL_GATEWAY",
    "NAT_GATEWAY",
    "NETWORK_INTERFACE",
    "VPC_ENDPOINT",
    "VPC_PEERING_CONNECTION",
    "EGRESS_ONLY_INTERNET_GATEWAY",
    "TRANSIT_GATEWAY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GATEWAY",
        "CARRIER_GATEWAY",
        "INSTANCE",
        "LOCAL_GATEWAY",
        "NAT_GATEWAY",
        "NETWORK_INTERFACE",
        "VPC_ENDPOINT",
        "VPC_PEERING_CONNECTION",
        "EGRESS_ONLY_INTERNET_GATEWAY",
        "TRANSIT_GATEWAY",
    )
)


def serialize_aws_json_1_1(value: TargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetType value: {data!r}")
    return cast(TargetType, data)
