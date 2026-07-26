"""Generated from Smithy shape ``com.amazonaws.ecrpublic#GetRepositoryPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr_public.types.registry_id
    import capo_ecr_public.types.repository_name


class GetRepositoryPolicyRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr_public.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID that's associated with the public registry that contains the repository. If you do not specify a registry, the default public registry is assumed.</p>"""
    repository_name: "capo_ecr_public.types.repository_name.RepositoryName"
    """<p>The name of the repository with the policy to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRepositoryPolicyRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRepositoryPolicyRequest:
    out: GetRepositoryPolicyRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "GetRepositoryPolicyRequest.repository_name required"
        )
    return out
