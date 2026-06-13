"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclUsers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_acl_user

DocumentAclUsers: TypeAlias = list[
    "aws_sdk_qbusiness.types.document_acl_user.DocumentAclUser"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclUsers) -> list:
    import aws_sdk_qbusiness.types.document_acl_user

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.document_acl_user.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentAclUsers:
    import aws_sdk_qbusiness.types.document_acl_user

    out: DocumentAclUsers = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.document_acl_user.deserialize_json(item))
    return out
