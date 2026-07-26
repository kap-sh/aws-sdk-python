"""Generated from Smithy shape ``com.amazonaws.securityir#ListMembershipItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_security_ir.types.list_membership_item

ListMembershipItems: TypeAlias = list[
    "capo_security_ir.types.list_membership_item.ListMembershipItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipItems) -> list:
    import capo_security_ir.types.list_membership_item

    out: list = []
    for item in value:
        out.append(capo_security_ir.types.list_membership_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListMembershipItems:
    import capo_security_ir.types.list_membership_item

    out: ListMembershipItems = []
    for item in data:
        out.append(capo_security_ir.types.list_membership_item.deserialize_json(item))
    return out
