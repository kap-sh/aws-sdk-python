"""Generated from Smithy shape ``com.amazonaws.ssm#ListResourceComplianceSummariesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.resource_compliance_summary_item_list


class ListResourceComplianceSummariesResult(TypedDict, closed=True):
    resource_compliance_summary_items: NotRequired[
        "capo_ssm.types.resource_compliance_summary_item_list.ResourceComplianceSummaryItemList"
    ]
    """<p>A summary count for specified or targeted managed nodes. Summary count includes information about compliant and non-compliant State Manager associations, patch status, or custom items according to the filter criteria that you specify. </p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceComplianceSummariesResult) -> dict:
    out: dict = {}
    if "resource_compliance_summary_items" in value:
        import capo_ssm.types.resource_compliance_summary_item_list

        out["ResourceComplianceSummaryItems"] = (
            capo_ssm.types.resource_compliance_summary_item_list.serialize_aws_json_1_1(
                value["resource_compliance_summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceComplianceSummariesResult:
    out: ListResourceComplianceSummariesResult = {}  # type: ignore[typeddict-item]
    if "ResourceComplianceSummaryItems" in data:
        import capo_ssm.types.resource_compliance_summary_item_list

        out["resource_compliance_summary_items"] = (
            capo_ssm.types.resource_compliance_summary_item_list.deserialize_aws_json_1_1(
                data["ResourceComplianceSummaryItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
