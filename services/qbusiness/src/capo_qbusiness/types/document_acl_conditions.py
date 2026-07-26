"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.document_acl_condition

DocumentAclConditions: TypeAlias = list[
    "capo_qbusiness.types.document_acl_condition.DocumentAclCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclConditions) -> list:
    import capo_qbusiness.types.document_acl_condition

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.document_acl_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentAclConditions:
    import capo_qbusiness.types.document_acl_condition

    out: DocumentAclConditions = []
    for item in data:
        out.append(capo_qbusiness.types.document_acl_condition.deserialize_json(item))
    return out
