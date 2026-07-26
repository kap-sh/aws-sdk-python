"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.document_acl_group

DocumentAclGroups: TypeAlias = list[
    "capo_qbusiness.types.document_acl_group.DocumentAclGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclGroups) -> list:
    import capo_qbusiness.types.document_acl_group

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.document_acl_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentAclGroups:
    import capo_qbusiness.types.document_acl_group

    out: DocumentAclGroups = []
    for item in data:
        out.append(capo_qbusiness.types.document_acl_group.deserialize_json(item))
    return out
