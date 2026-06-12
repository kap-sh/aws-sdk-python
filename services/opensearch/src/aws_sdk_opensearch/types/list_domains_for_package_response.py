"""Generated from Smithy shape ``com.amazonaws.opensearch#ListDomainsForPackageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_package_details_list
    import aws_sdk_opensearch.types.string


class ListDomainsForPackageResponse(TypedDict):
    domain_package_details_list: NotRequired[
        "aws_sdk_opensearch.types.domain_package_details_list.DomainPackageDetailsList"
    ]
    """<p>Information about all domains associated with a package.</p>"""
    next_token: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsForPackageResponse) -> dict:
    out: dict = {}
    if "domain_package_details_list" in value:
        import aws_sdk_opensearch.types.domain_package_details_list

        out["DomainPackageDetailsList"] = (
            aws_sdk_opensearch.types.domain_package_details_list.serialize_json(
                value["domain_package_details_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainsForPackageResponse:
    out: ListDomainsForPackageResponse = {}  # type: ignore[typeddict-item]
    if "DomainPackageDetailsList" in data:
        import aws_sdk_opensearch.types.domain_package_details_list

        out["domain_package_details_list"] = (
            aws_sdk_opensearch.types.domain_package_details_list.deserialize_json(
                data["DomainPackageDetailsList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
