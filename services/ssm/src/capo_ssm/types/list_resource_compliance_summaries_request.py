"""Generated from Smithy shape ``com.amazonaws.ssm#ListResourceComplianceSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.compliance_string_filter_list
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token


class ListResourceComplianceSummariesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_ssm.types.compliance_string_filter_list.ComplianceStringFilterList"
    ]
    """<p>One or more filters. Use a filter to return a more specific list of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceComplianceSummariesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_ssm.types.compliance_string_filter_list

        out["Filters"] = (
            capo_ssm.types.compliance_string_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceComplianceSummariesRequest:
    out: ListResourceComplianceSummariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_ssm.types.compliance_string_filter_list

        out["filters"] = (
            capo_ssm.types.compliance_string_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
