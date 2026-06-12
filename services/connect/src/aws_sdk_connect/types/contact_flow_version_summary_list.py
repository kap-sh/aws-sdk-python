"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_version_summary

ContactFlowVersionSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.contact_flow_version_summary.ContactFlowVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowVersionSummaryList) -> list:
    import aws_sdk_connect.types.contact_flow_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.contact_flow_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContactFlowVersionSummaryList:
    import aws_sdk_connect.types.contact_flow_version_summary

    out: ContactFlowVersionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.contact_flow_version_summary.deserialize_json(item)
        )
    return out
