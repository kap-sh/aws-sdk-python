"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeleteDomainPermissionsPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.policy_revision


class DeleteDomainPermissionsPolicyRequest(TypedDict):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain associated with the resource policy to be deleted. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    policy_revision: NotRequired[
        "aws_sdk_codeartifact.types.policy_revision.PolicyRevision"
    ]
    """<p> The current revision of the resource policy to be deleted. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain's resource policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainPermissionsPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainPermissionsPolicyRequest:
    out: DeleteDomainPermissionsPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
