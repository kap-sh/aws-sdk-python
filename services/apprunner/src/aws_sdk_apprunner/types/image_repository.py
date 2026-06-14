"""Generated from Smithy shape ``com.amazonaws.apprunner#ImageRepository``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.image_configuration
    import aws_sdk_apprunner.types.image_identifier
    import aws_sdk_apprunner.types.image_repository_type


class ImageRepository(TypedDict):
    image_identifier: "aws_sdk_apprunner.types.image_identifier.ImageIdentifier"
    r"""<p>The identifier of an image.</p> <p>For an image in Amazon Elastic Container Registry (Amazon ECR), this is an image name. For the image name format, see <a href=\"https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html\">Pulling an image</a> in the <i>Amazon ECR User Guide</i>.</p>"""
    image_configuration: NotRequired[
        "aws_sdk_apprunner.types.image_configuration.ImageConfiguration"
    ]
    """<p>Configuration for running the identified image.</p>"""
    image_repository_type: (
        "aws_sdk_apprunner.types.image_repository_type.ImageRepositoryType"
    )
    """<p>The type of the image repository. This reflects the repository provider and whether the repository is private or public.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImageRepository) -> dict:
    out: dict = {}
    out["ImageIdentifier"] = value["image_identifier"]
    if "image_configuration" in value:
        import aws_sdk_apprunner.types.image_configuration

        out["ImageConfiguration"] = (
            aws_sdk_apprunner.types.image_configuration.serialize_aws_json_1_0(
                value["image_configuration"]
            )
        )
    import aws_sdk_apprunner.types.image_repository_type

    out["ImageRepositoryType"] = (
        aws_sdk_apprunner.types.image_repository_type.serialize_aws_json_1_0(
            value["image_repository_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImageRepository:
    out: ImageRepository = {}  # type: ignore[typeddict-item]
    if "ImageIdentifier" in data:
        out["image_identifier"] = data["ImageIdentifier"]
    else:
        raise DeserializationError("ImageRepository.image_identifier required")
    if "ImageConfiguration" in data:
        import aws_sdk_apprunner.types.image_configuration

        out["image_configuration"] = (
            aws_sdk_apprunner.types.image_configuration.deserialize_aws_json_1_0(
                data["ImageConfiguration"]
            )
        )
    if "ImageRepositoryType" in data:
        import aws_sdk_apprunner.types.image_repository_type

        out["image_repository_type"] = (
            aws_sdk_apprunner.types.image_repository_type.deserialize_aws_json_1_0(
                data["ImageRepositoryType"]
            )
        )
    else:
        raise DeserializationError("ImageRepository.image_repository_type required")
    return out
