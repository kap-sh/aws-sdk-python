"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeImageSigningStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_identifier
    import aws_sdk_ecr.types.image_signing_status_list
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class DescribeImageSigningStatusResponse(TypedDict):
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The name of the repository.</p>"""
    image_id: NotRequired["aws_sdk_ecr.types.image_identifier.ImageIdentifier"]
    """<p>An object with identifying information for the image.</p>"""
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry.</p>"""
    signing_statuses: NotRequired[
        "aws_sdk_ecr.types.image_signing_status_list.ImageSigningStatusList"
    ]
    """<p>A list of signing statuses for the specified image. Each status corresponds to a signing profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageSigningStatusResponse) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "image_id" in value:
        import aws_sdk_ecr.types.image_identifier

        out["imageId"] = aws_sdk_ecr.types.image_identifier.serialize_aws_json_1_1(
            value["image_id"]
        )
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "signing_statuses" in value:
        import aws_sdk_ecr.types.image_signing_status_list

        out["signingStatuses"] = (
            aws_sdk_ecr.types.image_signing_status_list.serialize_aws_json_1_1(
                value["signing_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageSigningStatusResponse:
    out: DescribeImageSigningStatusResponse = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "imageId" in data:
        import aws_sdk_ecr.types.image_identifier

        out["image_id"] = aws_sdk_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "signingStatuses" in data:
        import aws_sdk_ecr.types.image_signing_status_list

        out["signing_statuses"] = (
            aws_sdk_ecr.types.image_signing_status_list.deserialize_aws_json_1_1(
                data["signingStatuses"]
            )
        )
    return out
