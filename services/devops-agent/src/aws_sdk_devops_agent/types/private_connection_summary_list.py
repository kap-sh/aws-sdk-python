"""Generated from Smithy shape ``com.amazonaws.devopsagent#PrivateConnectionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.private_connection_summary

PrivateConnectionSummaryList: TypeAlias = list[
    "aws_sdk_devops_agent.types.private_connection_summary.PrivateConnectionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionSummaryList) -> list:
    import aws_sdk_devops_agent.types.private_connection_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_agent.types.private_connection_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PrivateConnectionSummaryList:
    import aws_sdk_devops_agent.types.private_connection_summary

    out: PrivateConnectionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_devops_agent.types.private_connection_summary.deserialize_json(item)
        )
    return out
