"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_module

ContactFlowModuleSearchSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.contact_flow_module.ContactFlowModule"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleSearchSummaryList) -> list:
    import aws_sdk_connect.types.contact_flow_module

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.contact_flow_module.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactFlowModuleSearchSummaryList:
    import aws_sdk_connect.types.contact_flow_module

    out: ContactFlowModuleSearchSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.contact_flow_module.deserialize_json(item))
    return out
