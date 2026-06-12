"""Generated from Smithy shape ``com.amazonaws.chime#MembershipItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime.types.membership_item

MembershipItemList: TypeAlias = list[
    "aws_sdk_chime.types.membership_item.MembershipItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipItemList) -> list:
    import aws_sdk_chime.types.membership_item

    out: list = []
    for item in value:
        out.append(aws_sdk_chime.types.membership_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> MembershipItemList:
    import aws_sdk_chime.types.membership_item

    out: MembershipItemList = []
    for item in data:
        out.append(aws_sdk_chime.types.membership_item.deserialize_json(item))
    return out
