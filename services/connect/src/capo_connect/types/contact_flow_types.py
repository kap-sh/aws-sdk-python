"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_type

ContactFlowTypes: TypeAlias = list[
    "capo_connect.types.contact_flow_type.ContactFlowType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowTypes) -> list:
    import capo_connect.types.contact_flow_type

    out: list = []
    for item in value:
        out.append(capo_connect.types.contact_flow_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactFlowTypes:
    import capo_connect.types.contact_flow_type

    out: ContactFlowTypes = []
    for item in data:
        out.append(capo_connect.types.contact_flow_type.deserialize_json(item))
    return out
