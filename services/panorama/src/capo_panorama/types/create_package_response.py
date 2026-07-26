"""Generated from Smithy shape ``com.amazonaws.panorama#CreatePackageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.node_package_arn
    import capo_panorama.types.node_package_id
    import capo_panorama.types.storage_location


class CreatePackageResponse(TypedDict, closed=True):
    package_id: NotRequired["capo_panorama.types.node_package_id.NodePackageId"]
    """<p>The package's ID.</p>"""
    arn: NotRequired["capo_panorama.types.node_package_arn.NodePackageArn"]
    """<p>The package's ARN.</p>"""
    storage_location: "capo_panorama.types.storage_location.StorageLocation"
    """<p>The package's storage location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageResponse) -> dict:
    out: dict = {}
    if "package_id" in value:
        out["PackageId"] = value["package_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    import capo_panorama.types.storage_location

    out["StorageLocation"] = capo_panorama.types.storage_location.serialize_json(
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
        import capo_panorama.types.storage_location

        out["storage_location"] = capo_panorama.types.storage_location.deserialize_json(
            data["StorageLocation"]
        )
    else:
        raise DeserializationError("CreatePackageResponse.storage_location required")
    return out
