"""Generated from Smithy shape ``com.amazonaws.ssm#ListComplianceSummariesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.compliance_summary_item_list
    import capo_ssm.types.next_token


class ListComplianceSummariesResult(TypedDict, closed=True):
    compliance_summary_items: NotRequired[
        "capo_ssm.types.compliance_summary_item_list.ComplianceSummaryItemList"
    ]
    """<p>A list of compliant and non-compliant summary counts based on compliance types. For example, this call returns State Manager associations, patches, or custom compliance types according to the filter criteria that you specified.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListComplianceSummariesResult) -> dict:
    out: dict = {}
    if "compliance_summary_items" in value:
        import capo_ssm.types.compliance_summary_item_list

        out["ComplianceSummaryItems"] = (
            capo_ssm.types.compliance_summary_item_list.serialize_aws_json_1_1(
                value["compliance_summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListComplianceSummariesResult:
    out: ListComplianceSummariesResult = {}  # type: ignore[typeddict-item]
    if data.get("ComplianceSummaryItems") is not None:
        import capo_ssm.types.compliance_summary_item_list

        out["compliance_summary_items"] = (
            capo_ssm.types.compliance_summary_item_list.deserialize_aws_json_1_1(
                data["ComplianceSummaryItems"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
