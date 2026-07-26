"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.membership_type
    import capo_qbusiness.types.string


class DocumentAclUser(TypedDict, closed=True):
    id: NotRequired["capo_qbusiness.types.string.String"]
    """<p>The unique identifier of the user in the document's ACL. This is used to identify the user when applying access rules.</p>"""
    type: NotRequired["capo_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of the user. This indicates the scope of the user's applicability in access control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclUser) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> DocumentAclUser:
    out: DocumentAclUser = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.deserialize_json(
            data["type"]
        )
    return out
