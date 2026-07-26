"""Generated from Smithy shape ``com.amazonaws.qbusiness#CheckDocumentAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.associated_groups
    import capo_qbusiness.types.associated_users
    import capo_qbusiness.types.document_acl


class CheckDocumentAccessResponse(TypedDict, closed=True):
    user_groups: NotRequired["capo_qbusiness.types.associated_groups.AssociatedGroups"]
    """<p>An array of groups the user is part of for the specified data source. Each group has a name and type.</p>"""
    user_aliases: NotRequired["capo_qbusiness.types.associated_users.AssociatedUsers"]
    """<p>An array of aliases associated with the user. This includes both global and local aliases, each with a name and type.</p>"""
    has_access: NotRequired["bool"]
    """<p>A boolean value indicating whether the specified user has access to the document, either direct access or transitive access via groups and aliases attached to the document.</p>"""
    document_acl: NotRequired["capo_qbusiness.types.document_acl.DocumentAcl"]
    """<p>The Access Control List (ACL) associated with the document. Includes allowlist and denylist conditions that determine user access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckDocumentAccessResponse) -> dict:
    out: dict = {}
    if "user_groups" in value:
        import capo_qbusiness.types.associated_groups

        out["userGroups"] = capo_qbusiness.types.associated_groups.serialize_json(
            value["user_groups"]
        )
    if "user_aliases" in value:
        import capo_qbusiness.types.associated_users

        out["userAliases"] = capo_qbusiness.types.associated_users.serialize_json(
            value["user_aliases"]
        )
    if "has_access" in value:
        out["hasAccess"] = value["has_access"]
    if "document_acl" in value:
        import capo_qbusiness.types.document_acl

        out["documentAcl"] = capo_qbusiness.types.document_acl.serialize_json(
            value["document_acl"]
        )
    return out


def deserialize_json(data: dict) -> CheckDocumentAccessResponse:
    out: CheckDocumentAccessResponse = {}  # type: ignore[typeddict-item]
    if "userGroups" in data:
        import capo_qbusiness.types.associated_groups

        out["user_groups"] = capo_qbusiness.types.associated_groups.deserialize_json(
            data["userGroups"]
        )
    if "userAliases" in data:
        import capo_qbusiness.types.associated_users

        out["user_aliases"] = capo_qbusiness.types.associated_users.deserialize_json(
            data["userAliases"]
        )
    if "hasAccess" in data:
        out["has_access"] = data["hasAccess"]
    if "documentAcl" in data:
        import capo_qbusiness.types.document_acl

        out["document_acl"] = capo_qbusiness.types.document_acl.deserialize_json(
            data["documentAcl"]
        )
    return out
