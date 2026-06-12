"""Generated from Smithy shape ``com.amazonaws.opensearch#DeletePackageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.package_details


class DeletePackageResponse(TypedDict):
    package_details: NotRequired[
        "aws_sdk_opensearch.types.package_details.PackageDetails"
    ]
    """<p> Information about the deleted package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageResponse) -> dict:
    out: dict = {}
    if "package_details" in value:
        import aws_sdk_opensearch.types.package_details

        out["PackageDetails"] = aws_sdk_opensearch.types.package_details.serialize_json(
            value["package_details"]
        )
    return out


def deserialize_json(data: dict) -> DeletePackageResponse:
    out: DeletePackageResponse = {}  # type: ignore[typeddict-item]
    if "PackageDetails" in data:
        import aws_sdk_opensearch.types.package_details

        out["package_details"] = (
            aws_sdk_opensearch.types.package_details.deserialize_json(
                data["PackageDetails"]
            )
        )
    return out
