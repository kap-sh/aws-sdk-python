"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: PluginType) -> str:
    return value


def deserialize_json(data: str) -> PluginType:
    return cast(PluginType, data)
