"""Generated from Smithy shape ``com.amazonaws.opensearch#DissociatePackageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_package_details


class DissociatePackageResponse(TypedDict):
    domain_package_details: NotRequired[
        "aws_sdk_opensearch.types.domain_package_details.DomainPackageDetails"
    ]
    """<p> Information about a package that has been dissociated from the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DissociatePackageResponse) -> dict:
    out: dict = {}
    if "domain_package_details" in value:
        import aws_sdk_opensearch.types.domain_package_details

        out["DomainPackageDetails"] = (
            aws_sdk_opensearch.types.domain_package_details.serialize_json(
                value["domain_package_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> DissociatePackageResponse:
    out: DissociatePackageResponse = {}  # type: ignore[typeddict-item]
    if "DomainPackageDetails" in data:
        import aws_sdk_opensearch.types.domain_package_details

        out["domain_package_details"] = (
            aws_sdk_opensearch.types.domain_package_details.deserialize_json(
                data["DomainPackageDetails"]
            )
        )
    return out
