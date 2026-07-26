"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#DescribeReportDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.generic_string
    import capo_cost_and_usage_report_service.types.max_results


class DescribeReportDefinitionsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_cost_and_usage_report_service.types.max_results.MaxResults"
    ]
    next_token: NotRequired[
        "capo_cost_and_usage_report_service.types.generic_string.GenericString"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReportDefinitionsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReportDefinitionsRequest:
    out: DescribeReportDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
