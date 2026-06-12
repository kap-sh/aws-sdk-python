"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclUser``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.membership_type
    import aws_sdk_qbusiness.types.string

class DocumentAclUser(TypedDict):
    id: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The unique identifier of the user in the document's ACL. This is used to identify the user when applying access rules.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of the user. This indicates the scope of the user's applicability in access control.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclUser) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import aws_sdk_qbusiness.types.membership_type
        out["type"] = aws_sdk_qbusiness.types.membership_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> DocumentAclUser:
    out: DocumentAclUser = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        import aws_sdk_qbusiness.types.membership_type
        out["type"] = aws_sdk_qbusiness.types.membership_type.deserialize_json(data["type"])
    return out