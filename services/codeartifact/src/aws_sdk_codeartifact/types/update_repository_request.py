"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpdateRepositoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.description
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.repository_name
    import aws_sdk_codeartifact.types.upstream_repository_list


class UpdateRepositoryRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain associated with the repository to update. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository to update. </p>"""
    description: NotRequired["aws_sdk_codeartifact.types.description.Description"]
    """<p> An updated repository description. </p>"""
    upstreams: NotRequired[
        "aws_sdk_codeartifact.types.upstream_repository_list.UpstreamRepositoryList"
    ]
    r"""<p> A list of upstream repositories to associate with the repository. The order of the upstream repositories in the list determines their priority order when CodeArtifact looks for a requested package version. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html\">Working with upstream repositories</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRepositoryRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "upstreams" in value:
        import aws_sdk_codeartifact.types.upstream_repository_list

        out["upstreams"] = (
            aws_sdk_codeartifact.types.upstream_repository_list.serialize_json(
                value["upstreams"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRepositoryRequest:
    out: UpdateRepositoryRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "upstreams" in data:
        import aws_sdk_codeartifact.types.upstream_repository_list

        out["upstreams"] = (
            aws_sdk_codeartifact.types.upstream_repository_list.deserialize_json(
                data["upstreams"]
            )
        )
    return out
