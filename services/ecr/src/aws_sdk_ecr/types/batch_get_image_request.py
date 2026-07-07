"""Generated from Smithy shape ``com.amazonaws.ecr#BatchGetImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_identifier_list
    import aws_sdk_ecr.types.media_type_list
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class BatchGetImageRequest(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the images to describe. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The repository that contains the images to describe.</p>"""
    image_ids: "aws_sdk_ecr.types.image_identifier_list.ImageIdentifierList"
    """<p>A list of image ID references that correspond to images to describe. The format of the <code>imageIds</code> reference is <code>imageTag=tag</code> or <code>imageDigest=digest</code>.</p>"""
    accepted_media_types: NotRequired["aws_sdk_ecr.types.media_type_list.MediaTypeList"]
    """<p>The accepted media types for the request.</p> <p>Valid values: <code>application/vnd.docker.distribution.manifest.v1+json</code> | <code>application/vnd.docker.distribution.manifest.v2+json</code> | <code>application/vnd.oci.image.manifest.v1+json</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetImageRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    import aws_sdk_ecr.types.image_identifier_list

    out["imageIds"] = aws_sdk_ecr.types.image_identifier_list.serialize_aws_json_1_1(
        value["image_ids"]
    )
    if "accepted_media_types" in value:
        import aws_sdk_ecr.types.media_type_list

        out["acceptedMediaTypes"] = (
            aws_sdk_ecr.types.media_type_list.serialize_aws_json_1_1(
                value["accepted_media_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetImageRequest:
    out: BatchGetImageRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("BatchGetImageRequest.repository_name required")
    if "imageIds" in data:
        import aws_sdk_ecr.types.image_identifier_list

        out["image_ids"] = (
            aws_sdk_ecr.types.image_identifier_list.deserialize_aws_json_1_1(
                data["imageIds"]
            )
        )
    else:
        raise DeserializationError("BatchGetImageRequest.image_ids required")
    if "acceptedMediaTypes" in data:
        import aws_sdk_ecr.types.media_type_list

        out["accepted_media_types"] = (
            aws_sdk_ecr.types.media_type_list.deserialize_aws_json_1_1(
                data["acceptedMediaTypes"]
            )
        )
    return out
