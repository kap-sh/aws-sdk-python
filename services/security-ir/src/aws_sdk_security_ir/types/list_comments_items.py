"""Generated from Smithy shape ``com.amazonaws.securityir#ListCommentsItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.list_comments_item

ListCommentsItems: TypeAlias = list[
    "aws_sdk_security_ir.types.list_comments_item.ListCommentsItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListCommentsItems) -> list:
    import aws_sdk_security_ir.types.list_comments_item

    out: list = []
    for item in value:
        out.append(aws_sdk_security_ir.types.list_comments_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListCommentsItems:
    import aws_sdk_security_ir.types.list_comments_item

    out: ListCommentsItems = []
    for item in data:
        out.append(aws_sdk_security_ir.types.list_comments_item.deserialize_json(item))
    return out
