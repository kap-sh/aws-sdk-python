"""Generated from Smithy shape ``com.amazonaws.securityir#ListCasesItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.list_cases_item

ListCasesItems: TypeAlias = list[
    "aws_sdk_security_ir.types.list_cases_item.ListCasesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListCasesItems) -> list:
    import aws_sdk_security_ir.types.list_cases_item

    out: list = []
    for item in value:
        out.append(aws_sdk_security_ir.types.list_cases_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListCasesItems:
    import aws_sdk_security_ir.types.list_cases_item

    out: ListCasesItems = []
    for item in data:
        out.append(aws_sdk_security_ir.types.list_cases_item.deserialize_json(item))
    return out
