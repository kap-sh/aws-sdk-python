"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_module_version_summary

ContactFlowModuleVersionSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.contact_flow_module_version_summary.ContactFlowModuleVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleVersionSummaryList) -> list:
    import aws_sdk_connect.types.contact_flow_module_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.contact_flow_module_version_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ContactFlowModuleVersionSummaryList:
    import aws_sdk_connect.types.contact_flow_module_version_summary

    out: ContactFlowModuleVersionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.contact_flow_module_version_summary.deserialize_json(
                item
            )
        )
    return out
