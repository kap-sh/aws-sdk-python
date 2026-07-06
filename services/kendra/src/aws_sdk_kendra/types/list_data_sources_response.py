"""Generated from Smithy shape ``com.amazonaws.kendra#ListDataSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_summary_list
    import aws_sdk_kendra.types.next_token


class ListDataSourcesResponse(TypedDict, closed=True):
    summary_items: NotRequired[
        "aws_sdk_kendra.types.data_source_summary_list.DataSourceSummaryList"
    ]
    """<p>An array of summary information for one or more data source connector.</p>"""
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of data source connectors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataSourcesResponse) -> dict:
    out: dict = {}
    if "summary_items" in value:
        import aws_sdk_kendra.types.data_source_summary_list

        out["SummaryItems"] = (
            aws_sdk_kendra.types.data_source_summary_list.serialize_aws_json_1_1(
                value["summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataSourcesResponse:
    out: ListDataSourcesResponse = {}  # type: ignore[typeddict-item]
    if "SummaryItems" in data:
        import aws_sdk_kendra.types.data_source_summary_list

        out["summary_items"] = (
            aws_sdk_kendra.types.data_source_summary_list.deserialize_aws_json_1_1(
                data["SummaryItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
