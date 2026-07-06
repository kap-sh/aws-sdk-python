"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeImageReplicationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_identifier
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class DescribeImageReplicationStatusRequest(TypedDict, closed=True):
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository that the image is in.</p>"""
    image_id: "aws_sdk_ecr.types.image_identifier.ImageIdentifier"
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry. If you do not specify a registry, the default registry is assumed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageReplicationStatusRequest) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    import aws_sdk_ecr.types.image_identifier

    out["imageId"] = aws_sdk_ecr.types.image_identifier.serialize_aws_json_1_1(
        value["image_id"]
    )
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageReplicationStatusRequest:
    out: DescribeImageReplicationStatusRequest = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "DescribeImageReplicationStatusRequest.repository_name required"
        )
    if "imageId" in data:
        import aws_sdk_ecr.types.image_identifier

        out["image_id"] = aws_sdk_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    else:
        raise DeserializationError(
            "DescribeImageReplicationStatusRequest.image_id required"
        )
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    return out
