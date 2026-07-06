"""Generated from Smithy shape ``com.amazonaws.ecr#StartImageScanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_identifier
    import aws_sdk_ecr.types.image_scan_status
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class StartImageScanResponse(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    image_id: NotRequired["aws_sdk_ecr.types.image_identifier.ImageIdentifier"]
    image_scan_status: NotRequired[
        "aws_sdk_ecr.types.image_scan_status.ImageScanStatus"
    ]
    """<p>The current state of the scan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImageScanResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "image_id" in value:
        import aws_sdk_ecr.types.image_identifier

        out["imageId"] = aws_sdk_ecr.types.image_identifier.serialize_aws_json_1_1(
            value["image_id"]
        )
    if "image_scan_status" in value:
        import aws_sdk_ecr.types.image_scan_status

        out["imageScanStatus"] = (
            aws_sdk_ecr.types.image_scan_status.serialize_aws_json_1_1(
                value["image_scan_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImageScanResponse:
    out: StartImageScanResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "imageId" in data:
        import aws_sdk_ecr.types.image_identifier

        out["image_id"] = aws_sdk_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    if "imageScanStatus" in data:
        import aws_sdk_ecr.types.image_scan_status

        out["image_scan_status"] = (
            aws_sdk_ecr.types.image_scan_status.deserialize_aws_json_1_1(
                data["imageScanStatus"]
            )
        )
    return out
