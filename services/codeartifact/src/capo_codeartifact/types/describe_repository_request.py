"""Generated from Smithy shape ``com.amazonaws.codeartifact#DescribeRepositoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.repository_name


class DescribeRepositoryRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the repository to describe. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "capo_codeartifact.types.repository_name.RepositoryName"
    """<p> A string that specifies the name of the requested repository. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRepositoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRepositoryRequest:
    out: DescribeRepositoryRequest = {}  # type: ignore[typeddict-item]
    return out
