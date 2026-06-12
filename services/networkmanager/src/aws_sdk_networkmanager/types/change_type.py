"""Generated from Smithy shape ``com.amazonaws.networkmanager#ChangeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

ChangeType: TypeAlias = Literal[
    "CORE_NETWORK_SEGMENT",
    "NETWORK_FUNCTION_GROUP",
    "CORE_NETWORK_EDGE",
    "ATTACHMENT_MAPPING",
    "ATTACHMENT_ROUTE_PROPAGATION",
    "ATTACHMENT_ROUTE_STATIC",
    "ROUTING_POLICY",
    "ROUTING_POLICY_SEGMENT_ASSOCIATION",
    "ROUTING_POLICY_EDGE_ASSOCIATION",
    "ROUTING_POLICY_ATTACHMENT_ASSOCIATION",
    "CORE_NETWORK_CONFIGURATION",
    "SEGMENTS_CONFIGURATION",
    "SEGMENT_ACTIONS_CONFIGURATION",
    "ATTACHMENT_POLICIES_CONFIGURATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CORE_NETWORK_SEGMENT",
        "NETWORK_FUNCTION_GROUP",
        "CORE_NETWORK_EDGE",
        "ATTACHMENT_MAPPING",
        "ATTACHMENT_ROUTE_PROPAGATION",
        "ATTACHMENT_ROUTE_STATIC",
        "ROUTING_POLICY",
        "ROUTING_POLICY_SEGMENT_ASSOCIATION",
        "ROUTING_POLICY_EDGE_ASSOCIATION",
        "ROUTING_POLICY_ATTACHMENT_ASSOCIATION",
        "CORE_NETWORK_CONFIGURATION",
        "SEGMENTS_CONFIGURATION",
        "SEGMENT_ACTIONS_CONFIGURATION",
        "ATTACHMENT_POLICIES_CONFIGURATION",
    )
)


def serialize_json(value: ChangeType) -> str:
    return value


def deserialize_json(data: str) -> ChangeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeType value: {data!r}")
    return cast(ChangeType, data)
