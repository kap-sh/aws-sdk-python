"""Generated from Smithy shape ``com.amazonaws.opensearch#DissociatePackagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_package_details_list


class DissociatePackagesResponse(TypedDict, closed=True):
    domain_package_details_list: NotRequired[
        "capo_opensearch.types.domain_package_details_list.DomainPackageDetailsList"
    ]
    """<p>A list of package details for the packages that were dissociated from the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DissociatePackagesResponse) -> dict:
    out: dict = {}
    if "domain_package_details_list" in value:
        import capo_opensearch.types.domain_package_details_list

        out["DomainPackageDetailsList"] = (
            capo_opensearch.types.domain_package_details_list.serialize_json(
                value["domain_package_details_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> DissociatePackagesResponse:
    out: DissociatePackagesResponse = {}  # type: ignore[typeddict-item]
    if "DomainPackageDetailsList" in data:
        import capo_opensearch.types.domain_package_details_list

        out["domain_package_details_list"] = (
            capo_opensearch.types.domain_package_details_list.deserialize_json(
                data["DomainPackageDetailsList"]
            )
        )
    return out
