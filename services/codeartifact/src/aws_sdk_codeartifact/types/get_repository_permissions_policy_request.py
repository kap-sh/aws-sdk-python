"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetRepositoryPermissionsPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.repository_name


class GetRepositoryPermissionsPolicyRequest(TypedDict):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain containing the repository whose associated resource policy is to be retrieved. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository whose associated resource policy is to be retrieved. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRepositoryPermissionsPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRepositoryPermissionsPolicyRequest:
    out: GetRepositoryPermissionsPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
