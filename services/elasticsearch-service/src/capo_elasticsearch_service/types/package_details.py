"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PackageDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.created_at
    import capo_elasticsearch_service.types.error_details
    import capo_elasticsearch_service.types.last_updated
    import capo_elasticsearch_service.types.package_description
    import capo_elasticsearch_service.types.package_id
    import capo_elasticsearch_service.types.package_name
    import capo_elasticsearch_service.types.package_status
    import capo_elasticsearch_service.types.package_type
    import capo_elasticsearch_service.types.package_version


class PackageDetails(TypedDict, closed=True):
    package_id: NotRequired["capo_elasticsearch_service.types.package_id.PackageID"]
    """<p>Internal ID of the package.</p>"""
    package_name: NotRequired[
        "capo_elasticsearch_service.types.package_name.PackageName"
    ]
    """<p>User specified name of the package.</p>"""
    package_type: NotRequired[
        "capo_elasticsearch_service.types.package_type.PackageType"
    ]
    """<p>Currently supports only TXT-DICTIONARY.</p>"""
    package_description: NotRequired[
        "capo_elasticsearch_service.types.package_description.PackageDescription"
    ]
    """<p>User-specified description of the package.</p>"""
    package_status: NotRequired[
        "capo_elasticsearch_service.types.package_status.PackageStatus"
    ]
    """<p>Current state of the package. Values are COPYING/COPY_FAILED/AVAILABLE/DELETING/DELETE_FAILED</p>"""
    created_at: NotRequired["capo_elasticsearch_service.types.created_at.CreatedAt"]
    """<p>Timestamp which tells creation date of the package.</p>"""
    last_updated_at: NotRequired[
        "capo_elasticsearch_service.types.last_updated.LastUpdated"
    ]
    available_package_version: NotRequired[
        "capo_elasticsearch_service.types.package_version.PackageVersion"
    ]
    error_details: NotRequired[
        "capo_elasticsearch_service.types.error_details.ErrorDetails"
    ]
    """<p>Additional information if the package is in an error state. Null otherwise.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageDetails) -> dict:
    out: dict = {}
    if "package_id" in value:
        out["PackageID"] = value["package_id"]
    if "package_name" in value:
        out["PackageName"] = value["package_name"]
    if "package_type" in value:
        import capo_elasticsearch_service.types.package_type

        out["PackageType"] = (
            capo_elasticsearch_service.types.package_type.serialize_json(
                value["package_type"]
            )
        )
    if "package_description" in value:
        out["PackageDescription"] = value["package_description"]
    if "package_status" in value:
        import capo_elasticsearch_service.types.package_status

        out["PackageStatus"] = (
            capo_elasticsearch_service.types.package_status.serialize_json(
                value["package_status"]
            )
        )
    if "created_at" in value:
        import capo_elasticsearch_service.types.created_at

        out["CreatedAt"] = capo_elasticsearch_service.types.created_at.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_elasticsearch_service.types.last_updated

        out["LastUpdatedAt"] = (
            capo_elasticsearch_service.types.last_updated.serialize_json(
                value["last_updated_at"]
            )
        )
    if "available_package_version" in value:
        out["AvailablePackageVersion"] = value["available_package_version"]
    if "error_details" in value:
        import capo_elasticsearch_service.types.error_details

        out["ErrorDetails"] = (
            capo_elasticsearch_service.types.error_details.serialize_json(
                value["error_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageDetails:
    out: PackageDetails = {}  # type: ignore[typeddict-item]
    if "PackageID" in data:
        out["package_id"] = data["PackageID"]
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    if "PackageType" in data:
        import capo_elasticsearch_service.types.package_type

        out["package_type"] = (
            capo_elasticsearch_service.types.package_type.deserialize_json(
                data["PackageType"]
            )
        )
    if "PackageDescription" in data:
        out["package_description"] = data["PackageDescription"]
    if "PackageStatus" in data:
        import capo_elasticsearch_service.types.package_status

        out["package_status"] = (
            capo_elasticsearch_service.types.package_status.deserialize_json(
                data["PackageStatus"]
            )
        )
    if "CreatedAt" in data:
        import capo_elasticsearch_service.types.created_at

        out["created_at"] = (
            capo_elasticsearch_service.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import capo_elasticsearch_service.types.last_updated

        out["last_updated_at"] = (
            capo_elasticsearch_service.types.last_updated.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "AvailablePackageVersion" in data:
        out["available_package_version"] = data["AvailablePackageVersion"]
    if "ErrorDetails" in data:
        import capo_elasticsearch_service.types.error_details

        out["error_details"] = (
            capo_elasticsearch_service.types.error_details.deserialize_json(
                data["ErrorDetails"]
            )
        )
    return out
