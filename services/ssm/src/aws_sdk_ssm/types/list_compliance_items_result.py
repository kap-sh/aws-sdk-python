"""Generated from Smithy shape ``com.amazonaws.ssm#ListComplianceItemsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_item_list
    import aws_sdk_ssm.types.next_token


class ListComplianceItemsResult(TypedDict, closed=True):
    compliance_items: NotRequired[
        "aws_sdk_ssm.types.compliance_item_list.ComplianceItemList"
    ]
    """<p>A list of compliance information for the specified resource ID. </p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListComplianceItemsResult) -> dict:
    out: dict = {}
    if "compliance_items" in value:
        import aws_sdk_ssm.types.compliance_item_list

        out["ComplianceItems"] = (
            aws_sdk_ssm.types.compliance_item_list.serialize_aws_json_1_1(
                value["compliance_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListComplianceItemsResult:
    out: ListComplianceItemsResult = {}  # type: ignore[typeddict-item]
    if "ComplianceItems" in data:
        import aws_sdk_ssm.types.compliance_item_list

        out["compliance_items"] = (
            aws_sdk_ssm.types.compliance_item_list.deserialize_aws_json_1_1(
                data["ComplianceItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
