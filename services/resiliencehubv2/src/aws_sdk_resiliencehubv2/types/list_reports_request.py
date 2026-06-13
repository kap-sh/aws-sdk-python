"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListReportsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.max_results
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.report_type


class ListReportsRequest(TypedDict):
    service_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    """<p>Optional. If not provided, lists all reports owned by the account.</p>"""
    report_type: NotRequired["aws_sdk_resiliencehubv2.types.report_type.ReportType"]
    """<p>Filter reports by type.</p>"""
    max_results: "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListReportsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReportsRequest:
    out: ListReportsRequest = {}  # type: ignore[typeddict-item]
    return out
