"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateConformancePackComplianceSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_list
    import aws_sdk_config_service.types.next_token
    import aws_sdk_config_service.types.string_with_char_limit256


class GetAggregateConformancePackComplianceSummaryResponse(TypedDict, closed=True):
    aggregate_conformance_pack_compliance_summaries: NotRequired[
        "aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_list.AggregateConformancePackComplianceSummaryList"
    ]
    """<p>Returns a list of <code>AggregateConformancePackComplianceSummary</code> object.</p>"""
    group_by_key: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Groups the result based on Amazon Web Services account ID or Amazon Web Services Region.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetAggregateConformancePackComplianceSummaryResponse,
) -> dict:
    out: dict = {}
    if "aggregate_conformance_pack_compliance_summaries" in value:
        import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_list

        out["AggregateConformancePackComplianceSummaries"] = (
            aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_list.serialize_aws_json_1_1(
                value["aggregate_conformance_pack_compliance_summaries"]
            )
        )
    if "group_by_key" in value:
        out["GroupByKey"] = value["group_by_key"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetAggregateConformancePackComplianceSummaryResponse:
    out: GetAggregateConformancePackComplianceSummaryResponse = {}  # type: ignore[typeddict-item]
    if "AggregateConformancePackComplianceSummaries" in data:
        import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_list

        out["aggregate_conformance_pack_compliance_summaries"] = (
            aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_list.deserialize_aws_json_1_1(
                data["AggregateConformancePackComplianceSummaries"]
            )
        )
    if "GroupByKey" in data:
        out["group_by_key"] = data["GroupByKey"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
