"""Generated from Smithy shape ``com.amazonaws.securityir#ListMembershipItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.list_membership_item

ListMembershipItems: TypeAlias = list[
    "aws_sdk_security_ir.types.list_membership_item.ListMembershipItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipItems) -> list:
    import aws_sdk_security_ir.types.list_membership_item

    out: list = []
    for item in value:
        out.append(aws_sdk_security_ir.types.list_membership_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListMembershipItems:
    import aws_sdk_security_ir.types.list_membership_item

    out: ListMembershipItems = []
    for item in data:
        out.append(
            aws_sdk_security_ir.types.list_membership_item.deserialize_json(item)
        )
    return out
