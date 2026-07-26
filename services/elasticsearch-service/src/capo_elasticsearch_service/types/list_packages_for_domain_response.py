"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListPackagesForDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_package_details_list
    import capo_elasticsearch_service.types.string


class ListPackagesForDomainResponse(TypedDict, closed=True):
    domain_package_details_list: NotRequired[
        "capo_elasticsearch_service.types.domain_package_details_list.DomainPackageDetailsList"
    ]
    """<p>List of <code>DomainPackageDetails</code> objects.</p>"""
    next_token: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>Pagination token that needs to be supplied to the next call to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagesForDomainResponse) -> dict:
    out: dict = {}
    if "domain_package_details_list" in value:
        import capo_elasticsearch_service.types.domain_package_details_list

        out["DomainPackageDetailsList"] = (
            capo_elasticsearch_service.types.domain_package_details_list.serialize_json(
                value["domain_package_details_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPackagesForDomainResponse:
    out: ListPackagesForDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainPackageDetailsList" in data:
        import capo_elasticsearch_service.types.domain_package_details_list

        out["domain_package_details_list"] = (
            capo_elasticsearch_service.types.domain_package_details_list.deserialize_json(
                data["DomainPackageDetailsList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
