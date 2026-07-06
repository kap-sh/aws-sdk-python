"""Generated from Smithy shape ``com.amazonaws.opensearch#ListDirectQueryDataSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.direct_query_data_source_list
    import aws_sdk_opensearch.types.next_token


class ListDirectQueryDataSourcesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]
    direct_query_data_sources: NotRequired[
        "aws_sdk_opensearch.types.direct_query_data_source_list.DirectQueryDataSourceList"
    ]
    """<p> A list of the direct query data sources that are returned by the <code>ListDirectQueryDataSources</code> API operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDirectQueryDataSourcesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "direct_query_data_sources" in value:
        import aws_sdk_opensearch.types.direct_query_data_source_list

        out["DirectQueryDataSources"] = (
            aws_sdk_opensearch.types.direct_query_data_source_list.serialize_json(
                value["direct_query_data_sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDirectQueryDataSourcesResponse:
    out: ListDirectQueryDataSourcesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DirectQueryDataSources" in data:
        import aws_sdk_opensearch.types.direct_query_data_source_list

        out["direct_query_data_sources"] = (
            aws_sdk_opensearch.types.direct_query_data_source_list.deserialize_json(
                data["DirectQueryDataSources"]
            )
        )
    return out
