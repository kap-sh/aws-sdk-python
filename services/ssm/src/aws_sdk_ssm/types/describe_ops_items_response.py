"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeOpsItemsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_summaries
    import aws_sdk_ssm.types.string


class DescribeOpsItemsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""
    ops_item_summaries: NotRequired[
        "aws_sdk_ssm.types.ops_item_summaries.OpsItemSummaries"
    ]
    """<p>A list of OpsItems.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOpsItemsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "ops_item_summaries" in value:
        import aws_sdk_ssm.types.ops_item_summaries

        out["OpsItemSummaries"] = (
            aws_sdk_ssm.types.ops_item_summaries.serialize_aws_json_1_1(
                value["ops_item_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeOpsItemsResponse:
    out: DescribeOpsItemsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "OpsItemSummaries" in data:
        import aws_sdk_ssm.types.ops_item_summaries

        out["ops_item_summaries"] = (
            aws_sdk_ssm.types.ops_item_summaries.deserialize_aws_json_1_1(
                data["OpsItemSummaries"]
            )
        )
    return out
