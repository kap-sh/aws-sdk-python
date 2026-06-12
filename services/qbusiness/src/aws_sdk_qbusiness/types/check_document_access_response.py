"""Generated from Smithy shape ``com.amazonaws.qbusiness#CheckDocumentAccessResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.associated_groups
    import aws_sdk_qbusiness.types.associated_users
    import aws_sdk_qbusiness.types.document_acl

class CheckDocumentAccessResponse(TypedDict):
    user_groups: NotRequired["aws_sdk_qbusiness.types.associated_groups.AssociatedGroups"]
    """<p>An array of groups the user is part of for the specified data source. Each group has a name and type.</p>"""
    user_aliases: NotRequired["aws_sdk_qbusiness.types.associated_users.AssociatedUsers"]
    """<p>An array of aliases associated with the user. This includes both global and local aliases, each with a name and type.</p>"""
    has_access: NotRequired["bool"]
    """<p>A boolean value indicating whether the specified user has access to the document, either direct access or transitive access via groups and aliases attached to the document.</p>"""
    document_acl: NotRequired["aws_sdk_qbusiness.types.document_acl.DocumentAcl"]
    """<p>The Access Control List (ACL) associated with the document. Includes allowlist and denylist conditions that determine user access.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CheckDocumentAccessResponse) -> dict:
    out: dict = {}
    if "user_groups" in value:
        import aws_sdk_qbusiness.types.associated_groups
        out["userGroups"] = aws_sdk_qbusiness.types.associated_groups.serialize_json(value["user_groups"])
    if "user_aliases" in value:
        import aws_sdk_qbusiness.types.associated_users
        out["userAliases"] = aws_sdk_qbusiness.types.associated_users.serialize_json(value["user_aliases"])
    if "has_access" in value:
        out["hasAccess"] = value["has_access"]
    if "document_acl" in value:
        import aws_sdk_qbusiness.types.document_acl
        out["documentAcl"] = aws_sdk_qbusiness.types.document_acl.serialize_json(value["document_acl"])
    return out


def deserialize_json(data: dict) -> CheckDocumentAccessResponse:
    out: CheckDocumentAccessResponse = {}  # type: ignore[typeddict-item]
    if "userGroups" in data:
        import aws_sdk_qbusiness.types.associated_groups
        out["user_groups"] = aws_sdk_qbusiness.types.associated_groups.deserialize_json(data["userGroups"])
    if "userAliases" in data:
        import aws_sdk_qbusiness.types.associated_users
        out["user_aliases"] = aws_sdk_qbusiness.types.associated_users.deserialize_json(data["userAliases"])
    if "hasAccess" in data:
        out["has_access"] = data["hasAccess"]
    if "documentAcl" in data:
        import aws_sdk_qbusiness.types.document_acl
        out["document_acl"] = aws_sdk_qbusiness.types.document_acl.deserialize_json(data["documentAcl"])
    return out