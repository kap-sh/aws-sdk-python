"""Generated from Smithy shape ``com.amazonaws.route53domains#ViewBillingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.billing_records
    import aws_sdk_route_53_domains.types.page_marker


class ViewBillingResponse(TypedDict):
    next_page_marker: NotRequired[
        "aws_sdk_route_53_domains.types.page_marker.PageMarker"
    ]
    """<p>If there are more billing records than you specified for <code>MaxItems</code> in the request, submit another request and include the value of <code>NextPageMarker</code> in the value of <code>Marker</code>.</p>"""
    billing_records: NotRequired[
        "aws_sdk_route_53_domains.types.billing_records.BillingRecords"
    ]
    """<p>A summary of billing records.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewBillingResponse) -> dict:
    out: dict = {}
    if "next_page_marker" in value:
        out["NextPageMarker"] = value["next_page_marker"]
    if "billing_records" in value:
        import aws_sdk_route_53_domains.types.billing_records

        out["BillingRecords"] = (
            aws_sdk_route_53_domains.types.billing_records.serialize_aws_json_1_1(
                value["billing_records"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ViewBillingResponse:
    out: ViewBillingResponse = {}  # type: ignore[typeddict-item]
    if "NextPageMarker" in data:
        out["next_page_marker"] = data["NextPageMarker"]
    if "BillingRecords" in data:
        import aws_sdk_route_53_domains.types.billing_records

        out["billing_records"] = (
            aws_sdk_route_53_domains.types.billing_records.deserialize_aws_json_1_1(
                data["BillingRecords"]
            )
        )
    return out
