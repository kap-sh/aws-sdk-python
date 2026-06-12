"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectorProviderName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ConnectorProviderName: TypeAlias = Literal[
    "JIRA_CLOUD",
    "SERVICENOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JIRA_CLOUD",
        "SERVICENOW",
    )
)


def serialize_json(value: ConnectorProviderName) -> str:
    return value


def deserialize_json(data: str) -> ConnectorProviderName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorProviderName value: {data!r}")
    return cast(ConnectorProviderName, data)
