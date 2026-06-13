"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_acl_condition

DocumentAclConditions: TypeAlias = list[
    "aws_sdk_qbusiness.types.document_acl_condition.DocumentAclCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclConditions) -> list:
    import aws_sdk_qbusiness.types.document_acl_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.document_acl_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentAclConditions:
    import aws_sdk_qbusiness.types.document_acl_condition

    out: DocumentAclConditions = []
    for item in data:
        out.append(
            aws_sdk_qbusiness.types.document_acl_condition.deserialize_json(item)
        )
    return out
