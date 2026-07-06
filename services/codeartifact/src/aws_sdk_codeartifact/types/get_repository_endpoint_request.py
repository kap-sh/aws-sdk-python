"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetRepositoryEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.endpoint_type
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.repository_name


class GetRepositoryEndpointRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the repository. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces. </p>"""
    repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository. </p>"""
    format: "aws_sdk_codeartifact.types.package_format.PackageFormat"
    """<p> Returns which endpoint of a repository to return. A repository has one endpoint for each package format. </p>"""
    endpoint_type: NotRequired["aws_sdk_codeartifact.types.endpoint_type.EndpointType"]
    """<p>A string that specifies the type of endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRepositoryEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRepositoryEndpointRequest:
    out: GetRepositoryEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
