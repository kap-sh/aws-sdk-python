"""Generated from Smithy shape ``com.amazonaws.ecr#PutImageScanningConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_scanning_configuration
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class PutImageScanningConfigurationResponse(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    image_scanning_configuration: NotRequired[
        "aws_sdk_ecr.types.image_scanning_configuration.ImageScanningConfiguration"
    ]
    """<p>The image scanning configuration setting for the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutImageScanningConfigurationResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "image_scanning_configuration" in value:
        import aws_sdk_ecr.types.image_scanning_configuration

        out["imageScanningConfiguration"] = (
            aws_sdk_ecr.types.image_scanning_configuration.serialize_aws_json_1_1(
                value["image_scanning_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutImageScanningConfigurationResponse:
    out: PutImageScanningConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "imageScanningConfiguration" in data:
        import aws_sdk_ecr.types.image_scanning_configuration

        out["image_scanning_configuration"] = (
            aws_sdk_ecr.types.image_scanning_configuration.deserialize_aws_json_1_1(
                data["imageScanningConfiguration"]
            )
        )
    return out
