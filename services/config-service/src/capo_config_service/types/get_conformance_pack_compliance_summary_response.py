"""Generated from Smithy shape ``com.amazonaws.configservice#GetConformancePackComplianceSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_compliance_summary_list
    import capo_config_service.types.next_token


class GetConformancePackComplianceSummaryResponse(TypedDict, closed=True):
    conformance_pack_compliance_summary_list: NotRequired[
        "capo_config_service.types.conformance_pack_compliance_summary_list.ConformancePackComplianceSummaryList"
    ]
    """<p>A list of <code>ConformancePackComplianceSummary</code> objects. </p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConformancePackComplianceSummaryResponse) -> dict:
    out: dict = {}
    if "conformance_pack_compliance_summary_list" in value:
        import capo_config_service.types.conformance_pack_compliance_summary_list

        out["ConformancePackComplianceSummaryList"] = (
            capo_config_service.types.conformance_pack_compliance_summary_list.serialize_aws_json_1_1(
                value["conformance_pack_compliance_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConformancePackComplianceSummaryResponse:
    out: GetConformancePackComplianceSummaryResponse = {}  # type: ignore[typeddict-item]
    if "ConformancePackComplianceSummaryList" in data:
        import capo_config_service.types.conformance_pack_compliance_summary_list

        out["conformance_pack_compliance_summary_list"] = (
            capo_config_service.types.conformance_pack_compliance_summary_list.deserialize_aws_json_1_1(
                data["ConformancePackComplianceSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
