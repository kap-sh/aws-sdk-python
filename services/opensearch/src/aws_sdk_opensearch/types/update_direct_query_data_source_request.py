"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateDirectQueryDataSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.direct_query_data_source_description
    import aws_sdk_opensearch.types.direct_query_data_source_name
    import aws_sdk_opensearch.types.direct_query_data_source_type
    import aws_sdk_opensearch.types.direct_query_open_search_arn_list
    import aws_sdk_opensearch.types.policy_document


class UpdateDirectQueryDataSourceRequest(TypedDict):
    data_source_name: "aws_sdk_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName"
    """<p> A unique, user-defined label to identify the data source within your OpenSearch Service environment. </p>"""
    data_source_type: "aws_sdk_opensearch.types.direct_query_data_source_type.DirectQueryDataSourceType"
    """<p> The supported Amazon Web Services service that you want to use as the source for direct queries in OpenSearch Service. </p>"""
    description: NotRequired[
        "aws_sdk_opensearch.types.direct_query_data_source_description.DirectQueryDataSourceDescription"
    ]
    """<p> An optional text field for providing additional context and details about the data source. </p>"""
    open_search_arns: NotRequired[
        "aws_sdk_opensearch.types.direct_query_open_search_arn_list.DirectQueryOpenSearchARNList"
    ]
    """<p> An optional list of Amazon Resource Names (ARNs) for the OpenSearch collections that are associated with the direct query data source. This field is required for CloudWatchLogs and SecurityLake datasource types. </p>"""
    data_source_access_policy: NotRequired[
        "aws_sdk_opensearch.types.policy_document.PolicyDocument"
    ]
    """<p> An optional IAM access policy document that defines the updated permissions for accessing the direct query data source. The policy document must be in valid JSON format and follow IAM policy syntax. If not specified, the existing access policy if present remains unchanged. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDirectQueryDataSourceRequest) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> UpdateDirectQueryDataSourceRequest:
    out: UpdateDirectQueryDataSourceRequest = {}  # type: ignore[typeddict-item]
    if "DataSourceType" in data:
        import aws_sdk_opensearch.types.direct_query_data_source_type

        out["data_source_type"] = (
            aws_sdk_opensearch.types.direct_query_data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDirectQueryDataSourceRequest.data_source_type required"
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
    return out
