"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_flow

ContactFlowSearchSummaryList: TypeAlias = list[
    "capo_connect.types.contact_flow.ContactFlow"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowSearchSummaryList) -> list:
    import capo_connect.types.contact_flow

    out: list = []
    for item in value:
        out.append(capo_connect.types.contact_flow.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactFlowSearchSummaryList:
    import capo_connect.types.contact_flow

    out: ContactFlowSearchSummaryList = []
    for item in data:
        out.append(capo_connect.types.contact_flow.deserialize_json(item))
    return out
