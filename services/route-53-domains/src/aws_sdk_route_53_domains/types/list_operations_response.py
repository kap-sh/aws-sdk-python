"""Generated from Smithy shape ``com.amazonaws.route53domains#ListOperationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.operation_summary_list
    import aws_sdk_route_53_domains.types.page_marker


class ListOperationsResponse(TypedDict):
    operations: NotRequired[
        "aws_sdk_route_53_domains.types.operation_summary_list.OperationSummaryList"
    ]
    """<p>Lists summaries of the operations.</p>"""
    next_page_marker: NotRequired[
        "aws_sdk_route_53_domains.types.page_marker.PageMarker"
    ]
    """<p>If there are more operations than you specified for <code>MaxItems</code> in the request, submit another request and include the value of <code>NextPageMarker</code> in the value of <code>Marker</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOperationsResponse) -> dict:
    out: dict = {}
    if "operations" in value:
        import aws_sdk_route_53_domains.types.operation_summary_list

        out["Operations"] = (
            aws_sdk_route_53_domains.types.operation_summary_list.serialize_aws_json_1_1(
                value["operations"]
            )
        )
    if "next_page_marker" in value:
        out["NextPageMarker"] = value["next_page_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOperationsResponse:
    out: ListOperationsResponse = {}  # type: ignore[typeddict-item]
    if "Operations" in data:
        import aws_sdk_route_53_domains.types.operation_summary_list

        out["operations"] = (
            aws_sdk_route_53_domains.types.operation_summary_list.deserialize_aws_json_1_1(
                data["Operations"]
            )
        )
    if "NextPageMarker" in data:
        out["next_page_marker"] = data["NextPageMarker"]
    return out
