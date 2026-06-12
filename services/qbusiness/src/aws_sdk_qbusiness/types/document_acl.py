"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAcl``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_acl_membership

class DocumentAcl(TypedDict):
    allowlist: NotRequired["aws_sdk_qbusiness.types.document_acl_membership.DocumentAclMembership"]
    """<p>The allowlist conditions for the document. Users or groups matching these conditions are granted access to the document.</p>"""
    deny_list: NotRequired["aws_sdk_qbusiness.types.document_acl_membership.DocumentAclMembership"]
    """<p>The denylist conditions for the document. Users or groups matching these conditions are denied access to the document, overriding allowlist permissions.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DocumentAcl) -> dict:
    out: dict = {}
    if "allowlist" in value:
        import aws_sdk_qbusiness.types.document_acl_membership
        out["allowlist"] = aws_sdk_qbusiness.types.document_acl_membership.serialize_json(value["allowlist"])
    if "deny_list" in value:
        import aws_sdk_qbusiness.types.document_acl_membership
        out["denyList"] = aws_sdk_qbusiness.types.document_acl_membership.serialize_json(value["deny_list"])
    return out


def deserialize_json(data: dict) -> DocumentAcl:
    out: DocumentAcl = {}  # type: ignore[typeddict-item]
    if "allowlist" in data:
        import aws_sdk_qbusiness.types.document_acl_membership
        out["allowlist"] = aws_sdk_qbusiness.types.document_acl_membership.deserialize_json(data["allowlist"])
    if "denyList" in data:
        import aws_sdk_qbusiness.types.document_acl_membership
        out["deny_list"] = aws_sdk_qbusiness.types.document_acl_membership.deserialize_json(data["denyList"])
    return out