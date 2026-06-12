"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectorSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.connector_summary

ConnectorSummaryList: TypeAlias = list[
    "aws_sdk_securityhub.types.connector_summary.ConnectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorSummaryList) -> list:
    import aws_sdk_securityhub.types.connector_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.connector_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorSummaryList:
    import aws_sdk_securityhub.types.connector_summary

    out: ConnectorSummaryList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.connector_summary.deserialize_json(item))
    return out
