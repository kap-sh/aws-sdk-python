"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAutomationExecutionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_metadata_list
    import capo_ssm.types.next_token


class DescribeAutomationExecutionsResult(TypedDict, closed=True):
    automation_execution_metadata_list: NotRequired[
        "capo_ssm.types.automation_execution_metadata_list.AutomationExecutionMetadataList"
    ]
    """<p>The list of details about each automation execution which has occurred which matches the filter specification, if any.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAutomationExecutionsResult) -> dict:
    out: dict = {}
    if "automation_execution_metadata_list" in value:
        import capo_ssm.types.automation_execution_metadata_list

        out["AutomationExecutionMetadataList"] = (
            capo_ssm.types.automation_execution_metadata_list.serialize_aws_json_1_1(
                value["automation_execution_metadata_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAutomationExecutionsResult:
    out: DescribeAutomationExecutionsResult = {}  # type: ignore[typeddict-item]
    if data.get("AutomationExecutionMetadataList") is not None:
        import capo_ssm.types.automation_execution_metadata_list

        out["automation_execution_metadata_list"] = (
            capo_ssm.types.automation_execution_metadata_list.deserialize_aws_json_1_1(
                data["AutomationExecutionMetadataList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
