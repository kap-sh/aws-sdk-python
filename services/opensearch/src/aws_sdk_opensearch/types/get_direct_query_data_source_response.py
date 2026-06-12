"""Generated from Smithy shape ``com.amazonaws.opensearch#GetDirectQueryDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.direct_query_data_source_description
    import aws_sdk_opensearch.types.direct_query_data_source_name
    import aws_sdk_opensearch.types.direct_query_data_source_type
    import aws_sdk_opensearch.types.direct_query_open_search_arn_list
    import aws_sdk_opensearch.types.policy_document
    import aws_sdk_opensearch.types.string


class GetDirectQueryDataSourceResponse(TypedDict):
    data_source_name: NotRequired[
        "aws_sdk_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName"
    ]
    """<p> A unique, user-defined label to identify the data source within your OpenSearch Service environment. </p>"""
    data_source_type: NotRequired[
        "aws_sdk_opensearch.types.direct_query_data_source_type.DirectQueryDataSourceType"
    ]
    """<p> The supported Amazon Web Services service that is used as the source for direct queries in OpenSearch Service. </p>"""
    description: NotRequired[
        "aws_sdk_opensearch.types.direct_query_data_source_description.DirectQueryDataSourceDescription"
    ]
    """<p> A description that provides additional context and details about the data source. </p>"""
    open_search_arns: NotRequired[
        "aws_sdk_opensearch.types.direct_query_open_search_arn_list.DirectQueryOpenSearchARNList"
    ]
    """<p> A list of Amazon Resource Names (ARNs) for the OpenSearch collections that are associated with the direct query data source. </p>"""
    data_source_access_policy: NotRequired[
        "aws_sdk_opensearch.types.policy_document.PolicyDocument"
    ]
    """<p> The IAM access policy document that defines the permissions for accessing the direct query data source. Returns the current policy configuration in JSON format, or null if no custom policy is configured. </p>"""
    data_source_arn: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p> The unique, system-generated identifier that represents the data source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDirectQueryDataSourceResponse) -> dict:
    out: dict = {}
    if "data_source_name" in value:
        out["DataSourceName"] = value["data_source_name"]
    if "data_source_type" in value:
        import aws_sdk_opensearch.types.direct_query_data_source_type

        out["DataSourceType"] = (
            aws_sdk_opensearch.types.direct_query_data_source_type.serialize_json(
                value["data_source_type"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "open_search_arns" in value:
        import aws_sdk_opensearch.types.direct_query_open_search_arn_list

        out["OpenSearchArns"] = (
            aws_sdk_opensearch.types.direct_query_open_search_arn_list.serialize_json(
                value["open_search_arns"]
            )
        )
    if "data_source_access_policy" in value:
        out["DataSourceAccessPolicy"] = value["data_source_access_policy"]
    if "data_source_arn" in value:
        out["DataSourceArn"] = value["data_source_arn"]
    return out


def deserialize_json(data: dict) -> GetDirectQueryDataSourceResponse:
    out: GetDirectQueryDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "DataSourceName" in data:
        out["data_source_name"] = data["DataSourceName"]
    if "DataSourceType" in data:
        import aws_sdk_opensearch.types.direct_query_data_source_type

        out["data_source_type"] = (
            aws_sdk_opensearch.types.direct_query_data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "OpenSearchArns" in data:
        import aws_sdk_opensearch.types.direct_query_open_search_arn_list

        out["open_search_arns"] = (
            aws_sdk_opensearch.types.direct_query_open_search_arn_list.deserialize_json(
                data["OpenSearchArns"]
            )
        )
    if "DataSourceAccessPolicy" in data:
        out["data_source_access_policy"] = data["DataSourceAccessPolicy"]
    if "DataSourceArn" in data:
        out["data_source_arn"] = data["DataSourceArn"]
    return out
