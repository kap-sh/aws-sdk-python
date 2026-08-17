"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchCollection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.open_search_collection_endpoint
    import capo_cloudwatch_logs.types.open_search_resource_status


class OpenSearchCollection(TypedDict, closed=True):
    collection_endpoint: NotRequired[
        "capo_cloudwatch_logs.types.open_search_collection_endpoint.OpenSearchCollectionEndpoint"
    ]
    """<p>The endpoint of the collection.</p>"""
    collection_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the collection.</p>"""
    status: NotRequired[
        "capo_cloudwatch_logs.types.open_search_resource_status.OpenSearchResourceStatus"
    ]
    """<p>This structure contains information about the status of this OpenSearch Service resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenSearchCollection) -> dict:
    out: dict = {}
    if "collection_endpoint" in value:
        out["collectionEndpoint"] = value["collection_endpoint"]
    if "collection_arn" in value:
        out["collectionArn"] = value["collection_arn"]
    if "status" in value:
        import capo_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            capo_cloudwatch_logs.types.open_search_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenSearchCollection:
    out: OpenSearchCollection = {}  # type: ignore[typeddict-item]
    if data.get("collectionEndpoint") is not None:
        out["collection_endpoint"] = data["collectionEndpoint"]
    if data.get("collectionArn") is not None:
        out["collection_arn"] = data["collectionArn"]
    if data.get("status") is not None:
        import capo_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            capo_cloudwatch_logs.types.open_search_resource_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
