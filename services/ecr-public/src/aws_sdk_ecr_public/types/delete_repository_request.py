"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DeleteRepositoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.force_flag
    import aws_sdk_ecr_public.types.registry_id
    import aws_sdk_ecr_public.types.repository_name


class DeleteRepositoryRequest(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr_public.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID that's associated with the public registry that contains the repository to delete. If you do not specify a registry, the default public registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr_public.types.repository_name.RepositoryName"
    """<p>The name of the repository to delete.</p>"""
    force: "aws_sdk_ecr_public.types.force_flag.ForceFlag"
    """<p> The force option can be used to delete a repository that contains images. If the force option is not used, the repository must be empty prior to deletion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRepositoryRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["force"] = value.get("force", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRepositoryRequest:
    out: DeleteRepositoryRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("DeleteRepositoryRequest.repository_name required")
    if "force" in data:
        out["force"] = data["force"]
    else:
        out["force"] = False
    return out
