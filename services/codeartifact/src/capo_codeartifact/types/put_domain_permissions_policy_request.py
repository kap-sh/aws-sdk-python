"""Generated from Smithy shape ``com.amazonaws.codeartifact#PutDomainPermissionsPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.policy_document
    import capo_codeartifact.types.policy_revision


class PutDomainPermissionsPolicyRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain on which to set the resource policy. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    policy_revision: NotRequired[
        "capo_codeartifact.types.policy_revision.PolicyRevision"
    ]
    """<p> The current revision of the resource policy to be set. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain's resource policy. </p>"""
    policy_document: "capo_codeartifact.types.policy_document.PolicyDocument"
    """<p> A valid displayable JSON Aspen policy string to be set as the access control resource policy on the provided domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDomainPermissionsPolicyRequest) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    if "domain_owner" in value:
        out["domainOwner"] = value["domain_owner"]
    if "policy_revision" in value:
        out["policyRevision"] = value["policy_revision"]
    out["policyDocument"] = value["policy_document"]
    return out


def deserialize_json(data: dict) -> PutDomainPermissionsPolicyRequest:
    out: PutDomainPermissionsPolicyRequest = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("PutDomainPermissionsPolicyRequest.domain required")
    if "domainOwner" in data:
        out["domain_owner"] = data["domainOwner"]
    if "policyRevision" in data:
        out["policy_revision"] = data["policyRevision"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    else:
        raise DeserializationError(
            "PutDomainPermissionsPolicyRequest.policy_document required"
        )
    return out
