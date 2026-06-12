"""Generated from Smithy shape ``com.amazonaws.panorama#CreatePackageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.node_package_arn
    import aws_sdk_panorama.types.node_package_id
    import aws_sdk_panorama.types.storage_location


class CreatePackageResponse(TypedDict):
    package_id: NotRequired["aws_sdk_panorama.types.node_package_id.NodePackageId"]
    """<p>The package's ID.</p>"""
    arn: NotRequired["aws_sdk_panorama.types.node_package_arn.NodePackageArn"]
    """<p>The package's ARN.</p>"""
    storage_location: "aws_sdk_panorama.types.storage_location.StorageLocation"
    """<p>The package's storage location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageResponse) -> dict:
    out: dict = {}
    if "package_id" in value:
        out["PackageId"] = value["package_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    import aws_sdk_panorama.types.storage_location

    out["StorageLocation"] = aws_sdk_panorama.types.storage_location.serialize_json(
        value["storage_location"]
    )
    return out


def deserialize_json(data: dict) -> CreatePackageResponse:
    out: CreatePackageResponse = {}  # type: ignore[typeddict-item]
    if "PackageId" in data:
        out["package_id"] = data["PackageId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "StorageLocation" in data:
        import aws_sdk_panorama.types.storage_location

        out["storage_location"] = (
            aws_sdk_panorama.types.storage_location.deserialize_json(
                data["StorageLocation"]
            )
        )
    else:
        raise DeserializationError("CreatePackageResponse.storage_location required")
    return out
