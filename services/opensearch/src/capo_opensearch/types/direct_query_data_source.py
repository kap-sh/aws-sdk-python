"""Generated from Smithy shape ``com.amazonaws.opensearch#DirectQueryDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.direct_query_data_source_description
    import capo_opensearch.types.direct_query_data_source_name
    import capo_opensearch.types.direct_query_data_source_type
    import capo_opensearch.types.direct_query_open_search_arn_list
    import capo_opensearch.types.string
    import capo_opensearch.types.tag_list


class DirectQueryDataSource(TypedDict, closed=True):
    data_source_name: NotRequired[
        "capo_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName"
    ]
    """<p> A unique, user-defined label to identify the data source within your OpenSearch Service environment. </p>"""
    data_source_type: NotRequired[
        "capo_opensearch.types.direct_query_data_source_type.DirectQueryDataSourceType"
    ]
    """<p> The supported Amazon Web Services service that is used as the source for direct queries in OpenSearch Service. </p>"""
    description: NotRequired[
        "capo_opensearch.types.direct_query_data_source_description.DirectQueryDataSourceDescription"
    ]
    """<p> A description that provides additional context and details about the data source.</p>"""
    open_search_arns: NotRequired[
        "capo_opensearch.types.direct_query_open_search_arn_list.DirectQueryOpenSearchARNList"
    ]
    """<p> A list of Amazon Resource Names (ARNs) for the OpenSearch collections that are associated with the direct query data source. </p>"""
    data_source_arn: NotRequired["capo_opensearch.types.string.String"]
    """<p> The unique, system-generated identifier that represents the data source.</p>"""
    tag_list: NotRequired["capo_opensearch.types.tag_list.TagList"]
    """<p> A list of tags attached to a direct query data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DirectQueryDataSource) -> dict:
    out: dict = {}
    if "data_source_name" in value:
        out["DataSourceName"] = value["data_source_name"]
    if "data_source_type" in value:
        import capo_opensearch.types.direct_query_data_source_type

        out["DataSourceType"] = (
            capo_opensearch.types.direct_query_data_source_type.serialize_json(
                value["data_source_type"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "open_search_arns" in value:
        import capo_opensearch.types.direct_query_open_search_arn_list

        out["OpenSearchArns"] = (
            capo_opensearch.types.direct_query_open_search_arn_list.serialize_json(
                value["open_search_arns"]
            )
        )
    if "data_source_arn" in value:
        out["DataSourceArn"] = value["data_source_arn"]
    if "tag_list" in value:
        import capo_opensearch.types.tag_list

        out["TagList"] = capo_opensearch.types.tag_list.serialize_json(
            value["tag_list"]
        )
    return out


def deserialize_json(data: dict) -> DirectQueryDataSource:
    out: DirectQueryDataSource = {}  # type: ignore[typeddict-item]
    if "DataSourceName" in data:
        out["data_source_name"] = data["DataSourceName"]
    if "DataSourceType" in data:
        import capo_opensearch.types.direct_query_data_source_type

        out["data_source_type"] = (
            capo_opensearch.types.direct_query_data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "OpenSearchArns" in data:
        import capo_opensearch.types.direct_query_open_search_arn_list

        out["open_search_arns"] = (
            capo_opensearch.types.direct_query_open_search_arn_list.deserialize_json(
                data["OpenSearchArns"]
            )
        )
    if "DataSourceArn" in data:
        out["data_source_arn"] = data["DataSourceArn"]
    if "TagList" in data:
        import capo_opensearch.types.tag_list

        out["tag_list"] = capo_opensearch.types.tag_list.deserialize_json(
            data["TagList"]
        )
    return out
