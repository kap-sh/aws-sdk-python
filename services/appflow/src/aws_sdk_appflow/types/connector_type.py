"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: ConnectorType) -> str:
    return value


def deserialize_json(data: str) -> ConnectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorType value: {data!r}")
    return cast(ConnectorType, data)
