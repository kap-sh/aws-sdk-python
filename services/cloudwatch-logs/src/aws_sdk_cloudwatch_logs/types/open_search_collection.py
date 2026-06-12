"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchCollection``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.open_search_collection_endpoint
    import aws_sdk_cloudwatch_logs.types.open_search_resource_status


class OpenSearchCollection(TypedDict):
    collection_endpoint: NotRequired[
        "aws_sdk_cloudwatch_logs.types.open_search_collection_endpoint.OpenSearchCollectionEndpoint"
    ]
    """<p>The endpoint of the collection.</p>"""
    collection_arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the collection.</p>"""
    status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.open_search_resource_status.OpenSearchResourceStatus"
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
        import aws_sdk_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.open_search_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenSearchCollection:
    out: OpenSearchCollection = {}  # type: ignore[typeddict-item]
    if "collectionEndpoint" in data:
        out["collection_endpoint"] = data["collectionEndpoint"]
    if "collectionArn" in data:
        out["collection_arn"] = data["collectionArn"]
    if "status" in data:
        import aws_sdk_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.open_search_resource_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
