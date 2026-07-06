"""Generated from Smithy shape ``com.amazonaws.configservice#ListStoredQueriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.stored_query_metadata_list
    import aws_sdk_config_service.types.string


class ListStoredQueriesResponse(TypedDict, closed=True):
    stored_query_metadata: NotRequired[
        "aws_sdk_config_service.types.stored_query_metadata_list.StoredQueryMetadataList"
    ]
    """<p>A list of <code>StoredQueryMetadata</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this operation again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStoredQueriesResponse) -> dict:
    out: dict = {}
    if "stored_query_metadata" in value:
        import aws_sdk_config_service.types.stored_query_metadata_list

        out["StoredQueryMetadata"] = (
            aws_sdk_config_service.types.stored_query_metadata_list.serialize_aws_json_1_1(
                value["stored_query_metadata"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStoredQueriesResponse:
    out: ListStoredQueriesResponse = {}  # type: ignore[typeddict-item]
    if "StoredQueryMetadata" in data:
        import aws_sdk_config_service.types.stored_query_metadata_list

        out["stored_query_metadata"] = (
            aws_sdk_config_service.types.stored_query_metadata_list.deserialize_aws_json_1_1(
                data["StoredQueryMetadata"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
