"""Generated from Smithy shape ``com.amazonaws.ecr#StartImageScanRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_identifier
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class StartImageScanRequest(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository in which to start an image scan request. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the images to scan.</p>"""
    image_id: "aws_sdk_ecr.types.image_identifier.ImageIdentifier"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImageScanRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    import aws_sdk_ecr.types.image_identifier

    out["imageId"] = aws_sdk_ecr.types.image_identifier.serialize_aws_json_1_1(
        value["image_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImageScanRequest:
    out: StartImageScanRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("StartImageScanRequest.repository_name required")
    if "imageId" in data:
        import aws_sdk_ecr.types.image_identifier

        out["image_id"] = aws_sdk_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    else:
        raise DeserializationError("StartImageScanRequest.image_id required")
    return out
