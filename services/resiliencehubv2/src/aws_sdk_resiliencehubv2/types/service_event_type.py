"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

ServiceEventType: TypeAlias = Literal[
    "SERVICE_CREATED",
    "SERVICE_DELETED",
    "SERVICE_SYSTEM_ASSOCIATED",
    "SERVICE_SYSTEM_DISASSOCIATED",
    "SERVICE_RESOURCES_ASSOCIATED",
    "SERVICE_RESOURCES_DISASSOCIATED",
    "SERVICE_WORKFLOW_UPDATED",
    "SERVICE_INPUT_SOURCES_UPDATED",
    "SERVICE_POLICY_ASSOCIATED",
    "SERVICE_POLICY_DISASSOCIATED",
    "SERVICE_FUNCTION_CREATED",
    "SERVICE_FUNCTION_UPDATED",
    "SERVICE_FUNCTION_DELETED",
    "SERVICE_FUNCTION_RESOURCES_ADDED",
    "SERVICE_FUNCTION_RESOURCES_REMOVED",
    "SERVICE_ACHIEVABILITY_UPDATED",
    "ASSERTION_CREATED",
    "ASSERTION_UPDATED",
    "ASSERTION_DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE_CREATED",
        "SERVICE_DELETED",
        "SERVICE_SYSTEM_ASSOCIATED",
        "SERVICE_SYSTEM_DISASSOCIATED",
        "SERVICE_RESOURCES_ASSOCIATED",
        "SERVICE_RESOURCES_DISASSOCIATED",
        "SERVICE_WORKFLOW_UPDATED",
        "SERVICE_INPUT_SOURCES_UPDATED",
        "SERVICE_POLICY_ASSOCIATED",
        "SERVICE_POLICY_DISASSOCIATED",
        "SERVICE_FUNCTION_CREATED",
        "SERVICE_FUNCTION_UPDATED",
        "SERVICE_FUNCTION_DELETED",
        "SERVICE_FUNCTION_RESOURCES_ADDED",
        "SERVICE_FUNCTION_RESOURCES_REMOVED",
        "SERVICE_ACHIEVABILITY_UPDATED",
        "ASSERTION_CREATED",
        "ASSERTION_UPDATED",
        "ASSERTION_DELETED",
    )
)


def serialize_json(value: ServiceEventType) -> str:
    return value


def deserialize_json(data: str) -> ServiceEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceEventType value: {data!r}")
    return cast(ServiceEventType, data)
