"""Generated from Smithy shape ``com.amazonaws.qapps#PluginType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

PluginType: TypeAlias = Literal[
    "SERVICE_NOW",
    "SALESFORCE",
    "JIRA",
    "ZENDESK",
    "CUSTOM",
    "ASANA",
    "ATLASSIAN_CONFLUENCE",
    "GOOGLE_CALENDAR",
    "JIRA_CLOUD",
    "MICROSOFT_EXCHANGE",
    "MICROSOFT_TEAMS",
    "PAGERDUTY_ADVANCE",
    "SALESFORCE_CRM",
    "SERVICENOW_NOW_PLATFORM",
    "SMARTSHEET",
    "ZENDESK_SUITE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE_NOW",
        "SALESFORCE",
        "JIRA",
        "ZENDESK",
        "CUSTOM",
        "ASANA",
        "ATLASSIAN_CONFLUENCE",
        "GOOGLE_CALENDAR",
        "JIRA_CLOUD",
        "MICROSOFT_EXCHANGE",
        "MICROSOFT_TEAMS",
        "PAGERDUTY_ADVANCE",
        "SALESFORCE_CRM",
        "SERVICENOW_NOW_PLATFORM",
        "SMARTSHEET",
        "ZENDESK_SUITE",
    )
)


def serialize_json(value: PluginType) -> str:
    return value


def deserialize_json(data: str) -> PluginType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PluginType value: {data!r}")
    return cast(PluginType, data)
