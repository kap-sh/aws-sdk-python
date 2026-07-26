"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeleteRepositoryPermissionsPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.policy_revision
    import capo_codeartifact.types.repository_name


class DeleteRepositoryPermissionsPolicyRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the repository associated with the resource policy to be deleted. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "capo_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository that is associated with the resource policy to be deleted </p>"""
    policy_revision: NotRequired[
        "capo_codeartifact.types.policy_revision.PolicyRevision"
    ]
    """<p> The revision of the repository's resource policy to be deleted. This revision is used for optimistic locking, which prevents others from accidentally overwriting your changes to the repository's resource policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRepositoryPermissionsPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRepositoryPermissionsPolicyRequest:
    out: DeleteRepositoryPermissionsPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
