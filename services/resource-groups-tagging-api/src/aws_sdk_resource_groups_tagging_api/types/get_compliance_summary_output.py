"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GetComplianceSummaryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.pagination_token
    import aws_sdk_resource_groups_tagging_api.types.summary_list


class GetComplianceSummaryOutput(TypedDict, closed=True):
    summary_list: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.summary_list.SummaryList"
    ]
    """<p>A table that shows counts of noncompliant resources.</p>"""
    pagination_token: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.pagination_token.PaginationToken"
    ]
    """<p>A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the <code>PaginationToken</code> value in the request for the next page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceSummaryOutput) -> dict:
    out: dict = {}
    if "summary_list" in value:
        import aws_sdk_resource_groups_tagging_api.types.summary_list

        out["SummaryList"] = (
            aws_sdk_resource_groups_tagging_api.types.summary_list.serialize_aws_json_1_1(
                value["summary_list"]
            )
        )
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceSummaryOutput:
    out: GetComplianceSummaryOutput = {}  # type: ignore[typeddict-item]
    if "SummaryList" in data:
        import aws_sdk_resource_groups_tagging_api.types.summary_list

        out["summary_list"] = (
            aws_sdk_resource_groups_tagging_api.types.summary_list.deserialize_aws_json_1_1(
                data["SummaryList"]
            )
        )
    if "PaginationToken" in data:
        out["pagination_token"] = data["PaginationToken"]
    return out
