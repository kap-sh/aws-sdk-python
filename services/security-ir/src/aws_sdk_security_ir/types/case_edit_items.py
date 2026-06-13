"""Generated from Smithy shape ``com.amazonaws.securityir#CaseEditItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_edit_item

CaseEditItems: TypeAlias = list["aws_sdk_security_ir.types.case_edit_item.CaseEditItem"]


# --- restJson1 ser/de ---
def serialize_json(value: CaseEditItems) -> list:
    import aws_sdk_security_ir.types.case_edit_item

    out: list = []
    for item in value:
        out.append(aws_sdk_security_ir.types.case_edit_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaseEditItems:
    import aws_sdk_security_ir.types.case_edit_item

    out: CaseEditItems = []
    for item in data:
        out.append(aws_sdk_security_ir.types.case_edit_item.deserialize_json(item))
    return out
