"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowOperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

FlowOperationType: TypeAlias = Literal[
    "FLOW_FLUSH",
    "FLOW_CAPTURE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLOW_FLUSH",
        "FLOW_CAPTURE",
    )
)


def serialize_aws_json_1_0(value: FlowOperationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FlowOperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowOperationType value: {data!r}")
    return cast(FlowOperationType, data)
