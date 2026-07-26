"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorType``."""

from typing import Literal, TypeAlias, cast

ActionConnectorType: TypeAlias = Literal[
    "GENERIC_HTTP",
    "SERVICENOW_NOW_PLATFORM",
    "SALESFORCE_CRM",
    "MICROSOFT_OUTLOOK",
    "PAGERDUTY_ADVANCE",
    "JIRA_CLOUD",
    "ATLASSIAN_CONFLUENCE",
    "AMAZON_S3",
    "AMAZON_BEDROCK_AGENT_RUNTIME",
    "AMAZON_BEDROCK_RUNTIME",
    "AMAZON_BEDROCK_DATA_AUTOMATION_RUNTIME",
    "AMAZON_TEXTRACT",
    "AMAZON_COMPREHEND",
    "AMAZON_COMPREHEND_MEDICAL",
    "MICROSOFT_ONEDRIVE",
    "MICROSOFT_SHAREPOINT",
    "MICROSOFT_TEAMS",
    "SAP_BUSINESSPARTNER",
    "SAP_PRODUCTMASTERDATA",
    "SAP_PHYSICALINVENTORY",
    "SAP_BILLOFMATERIALS",
    "SAP_MATERIALSTOCK",
    "ZENDESK_SUITE",
    "SMARTSHEET",
    "SLACK",
    "ASANA",
    "BAMBOO_HR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnectorType) -> str:
    return value


def deserialize_json(data: str) -> ActionConnectorType:
    return cast(ActionConnectorType, data)
