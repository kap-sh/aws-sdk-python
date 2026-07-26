"""Generated from Smithy shape ``com.amazonaws.datazone#PolicyGrantMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.grant_identifier
    import capo_datazone.types.policy_grant_detail
    import capo_datazone.types.policy_grant_principal


class PolicyGrantMember(TypedDict, closed=True):
    principal: NotRequired[
        "capo_datazone.types.policy_grant_principal.PolicyGrantPrincipal"
    ]
    """<p>The principal of the policy grant member.</p>"""
    detail: NotRequired["capo_datazone.types.policy_grant_detail.PolicyGrantDetail"]
    """<p>The details of the policy grant member.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>Specifies the timestamp at which policy grant member was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>Specifies the user who created the policy grant member.</p>"""
    grant_id: NotRequired["capo_datazone.types.grant_identifier.GrantIdentifier"]
    """<p>The ID of the policy grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGrantMember) -> dict:
    out: dict = {}
    if "principal" in value:
        import capo_datazone.types.policy_grant_principal

        out["principal"] = capo_datazone.types.policy_grant_principal.serialize_json(
            value["principal"]
        )
    if "detail" in value:
        import capo_datazone.types.policy_grant_detail

        out["detail"] = capo_datazone.types.policy_grant_detail.serialize_json(
            value["detail"]
        )
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "grant_id" in value:
        out["grantId"] = value["grant_id"]
    return out


def deserialize_json(data: dict) -> PolicyGrantMember:
    out: PolicyGrantMember = {}  # type: ignore[typeddict-item]
    if "principal" in data:
        import capo_datazone.types.policy_grant_principal

        out["principal"] = capo_datazone.types.policy_grant_principal.deserialize_json(
            data["principal"]
        )
    if "detail" in data:
        import capo_datazone.types.policy_grant_detail

        out["detail"] = capo_datazone.types.policy_grant_detail.deserialize_json(
            data["detail"]
        )
    if "createdAt" in data:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "grantId" in data:
        out["grant_id"] = data["grantId"]
    return out
