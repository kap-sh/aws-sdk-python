"""Generated from Smithy shape ``com.amazonaws.qapps#PluginType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: PluginType) -> str:
    return value


def deserialize_json(data: str) -> PluginType:
    return cast(PluginType, data)
