"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.group_name
    import capo_qbusiness.types.membership_type


class DocumentAclGroup(TypedDict, closed=True):
    name: NotRequired["capo_qbusiness.types.group_name.GroupName"]
    """<p>The name of the group in the document's ACL. This is used to identify the group when applying access rules.</p>"""
    type: NotRequired["capo_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of the group. This indicates the scope of the group's applicability in access control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> DocumentAclGroup:
    out: DocumentAclGroup = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.deserialize_json(
            data["type"]
        )
    return out
