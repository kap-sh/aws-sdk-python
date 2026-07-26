"""Generated from Smithy shape ``com.amazonaws.ecr#UpdateImageStorageClassResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier
    import capo_ecr.types.image_status
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class UpdateImageStorageClassResponse(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["capo_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    image_id: NotRequired["capo_ecr.types.image_identifier.ImageIdentifier"]
    image_status: NotRequired["capo_ecr.types.image_status.ImageStatus"]
    """<p>The current status of the image after the call to UpdateImageStorageClass is complete. Valid values are <code>ACTIVE</code>, <code>ARCHIVED</code>, and <code>ACTIVATING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImageStorageClassResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "image_id" in value:
        import capo_ecr.types.image_identifier

        out["imageId"] = capo_ecr.types.image_identifier.serialize_aws_json_1_1(
            value["image_id"]
        )
    if "image_status" in value:
        import capo_ecr.types.image_status

        out["imageStatus"] = capo_ecr.types.image_status.serialize_aws_json_1_1(
            value["image_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateImageStorageClassResponse:
    out: UpdateImageStorageClassResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "imageId" in data:
        import capo_ecr.types.image_identifier

        out["image_id"] = capo_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    if "imageStatus" in data:
        import capo_ecr.types.image_status

        out["image_status"] = capo_ecr.types.image_status.deserialize_aws_json_1_1(
            data["imageStatus"]
        )
    return out
