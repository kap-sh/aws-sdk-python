"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModulesSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_module_summary

ContactFlowModulesSummaryList: TypeAlias = list[
    "capo_connect.types.contact_flow_module_summary.ContactFlowModuleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModulesSummaryList) -> list:
    import capo_connect.types.contact_flow_module_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.contact_flow_module_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactFlowModulesSummaryList:
    import capo_connect.types.contact_flow_module_summary

    out: ContactFlowModulesSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.contact_flow_module_summary.deserialize_json(item)
        )
    return out
