"""Generated from Smithy shape ``com.amazonaws.codeartifact#PutRepositoryPermissionsPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.policy_document
    import aws_sdk_codeartifact.types.policy_revision
    import aws_sdk_codeartifact.types.repository_name


class PutRepositoryPermissionsPolicyRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain containing the repository to set the resource policy on. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository to set the resource policy on. </p>"""
    policy_revision: NotRequired[
        "aws_sdk_codeartifact.types.policy_revision.PolicyRevision"
    ]
    """<p> Sets the revision of the resource policy that specifies permissions to access the repository. This revision is used for optimistic locking, which prevents others from overwriting your changes to the repository's resource policy. </p>"""
    policy_document: "aws_sdk_codeartifact.types.policy_document.PolicyDocument"
    """<p> A valid displayable JSON Aspen policy string to be set as the access control resource policy on the provided repository. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRepositoryPermissionsPolicyRequest) -> dict:
    out: dict = {}
    if "policy_revision" in value:
        out["policyRevision"] = value["policy_revision"]
    out["policyDocument"] = value["policy_document"]
    return out


def deserialize_json(data: dict) -> PutRepositoryPermissionsPolicyRequest:
    out: PutRepositoryPermissionsPolicyRequest = {}  # type: ignore[typeddict-item]
    if "policyRevision" in data:
        out["policy_revision"] = data["policyRevision"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    else:
        raise DeserializationError(
            "PutRepositoryPermissionsPolicyRequest.policy_document required"
        )
    return out
