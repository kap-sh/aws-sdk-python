"""Generated from Smithy shape ``com.amazonaws.ecr#UpdateImageStorageClassRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_identifier
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name
    import aws_sdk_ecr.types.target_storage_class


class UpdateImageStorageClassRequest(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the image to transition. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the image to transition.</p>"""
    image_id: "aws_sdk_ecr.types.image_identifier.ImageIdentifier"
    target_storage_class: "aws_sdk_ecr.types.target_storage_class.TargetStorageClass"
    """<p>The target storage class for the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImageStorageClassRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    import aws_sdk_ecr.types.image_identifier

    out["imageId"] = aws_sdk_ecr.types.image_identifier.serialize_aws_json_1_1(
        value["image_id"]
    )
    import aws_sdk_ecr.types.target_storage_class

    out["targetStorageClass"] = (
        aws_sdk_ecr.types.target_storage_class.serialize_aws_json_1_1(
            value["target_storage_class"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateImageStorageClassRequest:
    out: UpdateImageStorageClassRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "UpdateImageStorageClassRequest.repository_name required"
        )
    if "imageId" in data:
        import aws_sdk_ecr.types.image_identifier

        out["image_id"] = aws_sdk_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    else:
        raise DeserializationError("UpdateImageStorageClassRequest.image_id required")
    if "targetStorageClass" in data:
        import aws_sdk_ecr.types.target_storage_class

        out["target_storage_class"] = (
            aws_sdk_ecr.types.target_storage_class.deserialize_aws_json_1_1(
                data["targetStorageClass"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateImageStorageClassRequest.target_storage_class required"
        )
    return out
