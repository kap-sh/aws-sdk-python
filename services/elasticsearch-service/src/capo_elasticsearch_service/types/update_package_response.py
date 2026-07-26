"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpdatePackageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.package_details


class UpdatePackageResponse(TypedDict, closed=True):
    package_details: NotRequired[
        "capo_elasticsearch_service.types.package_details.PackageDetails"
    ]
    """<p>Information about the package <code>PackageDetails</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageResponse) -> dict:
    out: dict = {}
    if "package_details" in value:
        import capo_elasticsearch_service.types.package_details

        out["PackageDetails"] = (
            capo_elasticsearch_service.types.package_details.serialize_json(
                value["package_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePackageResponse:
    out: UpdatePackageResponse = {}  # type: ignore[typeddict-item]
    if "PackageDetails" in data:
        import capo_elasticsearch_service.types.package_details

        out["package_details"] = (
            capo_elasticsearch_service.types.package_details.deserialize_json(
                data["PackageDetails"]
            )
        )
    return out
