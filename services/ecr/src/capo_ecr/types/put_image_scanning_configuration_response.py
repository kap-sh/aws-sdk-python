"""Generated from Smithy shape ``com.amazonaws.ecr#PutImageScanningConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_scanning_configuration
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class PutImageScanningConfigurationResponse(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["capo_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    image_scanning_configuration: NotRequired[
        "capo_ecr.types.image_scanning_configuration.ImageScanningConfiguration"
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
        import capo_ecr.types.image_scanning_configuration

        out["imageScanningConfiguration"] = (
            capo_ecr.types.image_scanning_configuration.serialize_aws_json_1_1(
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
        import capo_ecr.types.image_scanning_configuration

        out["image_scanning_configuration"] = (
            capo_ecr.types.image_scanning_configuration.deserialize_aws_json_1_1(
                data["imageScanningConfiguration"]
            )
        )
    return out
