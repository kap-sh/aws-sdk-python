"""Generated from Smithy shape ``com.amazonaws.securityir#GetMembershipAccountDetailItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.get_membership_account_detail_item

GetMembershipAccountDetailItems: TypeAlias = list[
    "aws_sdk_security_ir.types.get_membership_account_detail_item.GetMembershipAccountDetailItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetMembershipAccountDetailItems) -> list:
    import aws_sdk_security_ir.types.get_membership_account_detail_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_security_ir.types.get_membership_account_detail_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GetMembershipAccountDetailItems:
    import aws_sdk_security_ir.types.get_membership_account_detail_item

    out: GetMembershipAccountDetailItems = []
    for item in data:
        out.append(
            aws_sdk_security_ir.types.get_membership_account_detail_item.deserialize_json(
                item
            )
        )
    return out
