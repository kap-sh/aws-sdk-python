"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclUsers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.document_acl_user

DocumentAclUsers: TypeAlias = list[
    "capo_qbusiness.types.document_acl_user.DocumentAclUser"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclUsers) -> list:
    import capo_qbusiness.types.document_acl_user

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.document_acl_user.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentAclUsers:
    import capo_qbusiness.types.document_acl_user

    out: DocumentAclUsers = []
    for item in data:
        out.append(capo_qbusiness.types.document_acl_user.deserialize_json(item))
    return out
