"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.group_name
    import aws_sdk_qbusiness.types.membership_type

class DocumentAclGroup(TypedDict):
    name: NotRequired["aws_sdk_qbusiness.types.group_name.GroupName"]
    """<p>The name of the group in the document's ACL. This is used to identify the group when applying access rules.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of the group. This indicates the scope of the group's applicability in access control.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_qbusiness.types.membership_type
        out["type"] = aws_sdk_qbusiness.types.membership_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> DocumentAclGroup:
    out: DocumentAclGroup = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import aws_sdk_qbusiness.types.membership_type
        out["type"] = aws_sdk_qbusiness.types.membership_type.deserialize_json(data["type"])
    return out