"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeleteDomainPermissionsPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.policy_revision


class DeleteDomainPermissionsPolicyRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain associated with the resource policy to be deleted. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    policy_revision: NotRequired[
        "capo_codeartifact.types.policy_revision.PolicyRevision"
    ]
    """<p> The current revision of the resource policy to be deleted. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain's resource policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainPermissionsPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainPermissionsPolicyRequest:
    out: DeleteDomainPermissionsPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
