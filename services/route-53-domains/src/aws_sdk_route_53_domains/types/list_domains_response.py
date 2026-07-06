"""Generated from Smithy shape ``com.amazonaws.route53domains#ListDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_summary_list
    import aws_sdk_route_53_domains.types.page_marker


class ListDomainsResponse(TypedDict, closed=True):
    domains: NotRequired[
        "aws_sdk_route_53_domains.types.domain_summary_list.DomainSummaryList"
    ]
    """<p>A list of domains.</p>"""
    next_page_marker: NotRequired[
        "aws_sdk_route_53_domains.types.page_marker.PageMarker"
    ]
    """<p>If there are more domains than you specified for <code>MaxItems</code> in the request, submit another request and include the value of <code>NextPageMarker</code> in the value of <code>Marker</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDomainsResponse) -> dict:
    out: dict = {}
    if "domains" in value:
        import aws_sdk_route_53_domains.types.domain_summary_list

        out["Domains"] = (
            aws_sdk_route_53_domains.types.domain_summary_list.serialize_aws_json_1_1(
                value["domains"]
            )
        )
    if "next_page_marker" in value:
        out["NextPageMarker"] = value["next_page_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDomainsResponse:
    out: ListDomainsResponse = {}  # type: ignore[typeddict-item]
    if "Domains" in data:
        import aws_sdk_route_53_domains.types.domain_summary_list

        out["domains"] = (
            aws_sdk_route_53_domains.types.domain_summary_list.deserialize_aws_json_1_1(
                data["Domains"]
            )
        )
    if "NextPageMarker" in data:
        out["next_page_marker"] = data["NextPageMarker"]
    return out
