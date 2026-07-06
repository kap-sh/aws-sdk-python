"""Generated from Smithy shape ``com.amazonaws.opensearch#CreatePackageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.package_details


class CreatePackageResponse(TypedDict, closed=True):
    package_details: NotRequired[
        "aws_sdk_opensearch.types.package_details.PackageDetails"
    ]
    """<p>Basic information about an OpenSearch Service package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageResponse) -> dict:
    out: dict = {}
    if "package_details" in value:
        import aws_sdk_opensearch.types.package_details

        out["PackageDetails"] = aws_sdk_opensearch.types.package_details.serialize_json(
            value["package_details"]
        )
    return out


def deserialize_json(data: dict) -> CreatePackageResponse:
    out: CreatePackageResponse = {}  # type: ignore[typeddict-item]
    if "PackageDetails" in data:
        import aws_sdk_opensearch.types.package_details

        out["package_details"] = (
            aws_sdk_opensearch.types.package_details.deserialize_json(
                data["PackageDetails"]
            )
        )
    return out
