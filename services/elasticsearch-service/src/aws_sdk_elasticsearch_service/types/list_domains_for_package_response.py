"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListDomainsForPackageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_package_details_list
    import aws_sdk_elasticsearch_service.types.string


class ListDomainsForPackageResponse(TypedDict, closed=True):
    domain_package_details_list: NotRequired[
        "aws_sdk_elasticsearch_service.types.domain_package_details_list.DomainPackageDetailsList"
    ]
    """<p>List of <code>DomainPackageDetails</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsForPackageResponse) -> dict:
    out: dict = {}
    if "domain_package_details_list" in value:
        import aws_sdk_elasticsearch_service.types.domain_package_details_list

        out["DomainPackageDetailsList"] = (
            aws_sdk_elasticsearch_service.types.domain_package_details_list.serialize_json(
                value["domain_package_details_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainsForPackageResponse:
    out: ListDomainsForPackageResponse = {}  # type: ignore[typeddict-item]
    if "DomainPackageDetailsList" in data:
        import aws_sdk_elasticsearch_service.types.domain_package_details_list

        out["domain_package_details_list"] = (
            aws_sdk_elasticsearch_service.types.domain_package_details_list.deserialize_json(
                data["DomainPackageDetailsList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
