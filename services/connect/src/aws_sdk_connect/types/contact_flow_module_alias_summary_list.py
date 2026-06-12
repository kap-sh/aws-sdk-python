"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleAliasSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_module_alias_summary

ContactFlowModuleAliasSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.contact_flow_module_alias_summary.ContactFlowModuleAliasSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleAliasSummaryList) -> list:
    import aws_sdk_connect.types.contact_flow_module_alias_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.contact_flow_module_alias_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContactFlowModuleAliasSummaryList:
    import aws_sdk_connect.types.contact_flow_module_alias_summary

    out: ContactFlowModuleAliasSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.contact_flow_module_alias_summary.deserialize_json(
                item
            )
        )
    return out
