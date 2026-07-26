"""Generated from Smithy shape ``com.amazonaws.opensearch#AssociatePackageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_package_details


class AssociatePackageResponse(TypedDict, closed=True):
    domain_package_details: NotRequired[
        "capo_opensearch.types.domain_package_details.DomainPackageDetails"
    ]
    """<p>Information about a package that is associated with a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePackageResponse) -> dict:
    out: dict = {}
    if "domain_package_details" in value:
        import capo_opensearch.types.domain_package_details

        out["DomainPackageDetails"] = (
            capo_opensearch.types.domain_package_details.serialize_json(
                value["domain_package_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociatePackageResponse:
    out: AssociatePackageResponse = {}  # type: ignore[typeddict-item]
    if "DomainPackageDetails" in data:
        import capo_opensearch.types.domain_package_details

        out["domain_package_details"] = (
            capo_opensearch.types.domain_package_details.deserialize_json(
                data["DomainPackageDetails"]
            )
        )
    return out
