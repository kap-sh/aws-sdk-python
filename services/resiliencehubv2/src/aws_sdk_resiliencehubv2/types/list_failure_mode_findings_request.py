"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListFailureModeFindingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.failure_category
    import aws_sdk_resiliencehubv2.types.finding_severity
    import aws_sdk_resiliencehubv2.types.finding_status
    import aws_sdk_resiliencehubv2.types.max_results
    import aws_sdk_resiliencehubv2.types.next_token


class ListFailureModeFindingsRequest(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    severity: NotRequired[
        "aws_sdk_resiliencehubv2.types.finding_severity.FindingSeverity"
    ]
    """<p>Filter findings by severity.</p>"""
    failure_category: NotRequired[
        "aws_sdk_resiliencehubv2.types.failure_category.FailureCategory"
    ]
    """<p>Filter findings by failure category.</p>"""
    status: NotRequired["aws_sdk_resiliencehubv2.types.finding_status.FindingStatus"]
    """<p>Filter findings by status.</p>"""
    max_results: "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListFailureModeFindingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFailureModeFindingsRequest:
    out: ListFailureModeFindingsRequest = {}  # type: ignore[typeddict-item]
    return out
