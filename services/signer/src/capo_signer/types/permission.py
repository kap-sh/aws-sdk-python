"""Generated from Smithy shape ``com.amazonaws.signer#Permission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.profile_version
    import capo_signer.types.string


class Permission(TypedDict, closed=True):
    action: NotRequired["capo_signer.types.string.String"]
    """<p>An AWS Signer action permitted as part of cross-account permissions.</p>"""
    principal: NotRequired["capo_signer.types.string.String"]
    """<p>The AWS principal that has been granted a cross-account permission.</p>"""
    statement_id: NotRequired["capo_signer.types.string.String"]
    """<p>A unique identifier for a cross-account permission statement.</p>"""
    profile_version: NotRequired["capo_signer.types.profile_version.ProfileVersion"]
    """<p>The signing profile version that a permission applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Permission) -> dict:
    out: dict = {}
    if "action" in value:
        out["action"] = value["action"]
    if "principal" in value:
        out["principal"] = value["principal"]
    if "statement_id" in value:
        out["statementId"] = value["statement_id"]
    if "profile_version" in value:
        out["profileVersion"] = value["profile_version"]
    return out


def deserialize_json(data: dict) -> Permission:
    out: Permission = {}  # type: ignore[typeddict-item]
    if "action" in data:
        out["action"] = data["action"]
    if "principal" in data:
        out["principal"] = data["principal"]
    if "statementId" in data:
        out["statement_id"] = data["statementId"]
    if "profileVersion" in data:
        out["profile_version"] = data["profileVersion"]
    return out
