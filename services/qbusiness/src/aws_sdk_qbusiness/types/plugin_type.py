"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

PluginType: TypeAlias = Literal[
    "SERVICE_NOW",
    "SALESFORCE",
    "JIRA",
    "ZENDESK",
    "CUSTOM",
    "QUICKSIGHT",
    "SERVICENOW_NOW_PLATFORM",
    "JIRA_CLOUD",
    "SALESFORCE_CRM",
    "ZENDESK_SUITE",
    "ATLASSIAN_CONFLUENCE",
    "GOOGLE_CALENDAR",
    "MICROSOFT_TEAMS",
    "MICROSOFT_EXCHANGE",
    "PAGERDUTY_ADVANCE",
    "SMARTSHEET",
    "ASANA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE_NOW",
        "SALESFORCE",
        "JIRA",
        "ZENDESK",
        "CUSTOM",
        "QUICKSIGHT",
        "SERVICENOW_NOW_PLATFORM",
        "JIRA_CLOUD",
        "SALESFORCE_CRM",
        "ZENDESK_SUITE",
        "ATLASSIAN_CONFLUENCE",
        "GOOGLE_CALENDAR",
        "MICROSOFT_TEAMS",
        "MICROSOFT_EXCHANGE",
        "PAGERDUTY_ADVANCE",
        "SMARTSHEET",
        "ASANA",
    )
)


def serialize_json(value: PluginType) -> str:
    return value


def deserialize_json(data: str) -> PluginType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PluginType value: {data!r}")
    return cast(PluginType, data)
