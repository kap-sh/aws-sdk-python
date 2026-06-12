"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeleteAgentErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

DeleteAgentErrorCode: TypeAlias = Literal[
    "NOT_FOUND",
    "INTERNAL_SERVER_ERROR",
    "AGENT_IN_USE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_FOUND",
        "INTERNAL_SERVER_ERROR",
        "AGENT_IN_USE",
    )
)


def serialize_aws_json_1_1(value: DeleteAgentErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeleteAgentErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeleteAgentErrorCode value: {data!r}")
    return cast(DeleteAgentErrorCode, data)
