"""Generated from Smithy shape ``com.amazonaws.securityir#CaseAttachmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_attachment_attributes

CaseAttachmentsList: TypeAlias = list[
    "aws_sdk_security_ir.types.case_attachment_attributes.CaseAttachmentAttributes"
]


# --- restJson1 ser/de ---
def serialize_json(value: CaseAttachmentsList) -> list:
    import aws_sdk_security_ir.types.case_attachment_attributes

    out: list = []
    for item in value:
        out.append(
            aws_sdk_security_ir.types.case_attachment_attributes.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CaseAttachmentsList:
    import aws_sdk_security_ir.types.case_attachment_attributes

    out: CaseAttachmentsList = []
    for item in data:
        out.append(
            aws_sdk_security_ir.types.case_attachment_attributes.deserialize_json(item)
        )
    return out
