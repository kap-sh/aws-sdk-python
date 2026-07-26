"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorType``."""

from typing import Literal, TypeAlias, cast

ConnectorType: TypeAlias = Literal[
    "Salesforce",
    "Singular",
    "Slack",
    "Redshift",
    "S3",
    "Marketo",
    "Googleanalytics",
    "Zendesk",
    "Servicenow",
    "Datadog",
    "Trendmicro",
    "Snowflake",
    "Dynatrace",
    "Infornexus",
    "Amplitude",
    "Veeva",
    "EventBridge",
    "LookoutMetrics",
    "Upsolver",
    "Honeycode",
    "CustomerProfiles",
    "SAPOData",
    "CustomConnector",
    "Pardot",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorType) -> str:
    return value


def deserialize_json(data: str) -> ConnectorType:
    return cast(ConnectorType, data)
