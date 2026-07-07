"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetCollectionGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_details
    import aws_sdk_opensearchserverless.types.collection_group_error_details


class BatchGetCollectionGroupResponse(TypedDict, closed=True):
    collection_group_details: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_details.CollectionGroupDetails"
    ]
    """<p>Details about each collection group.</p>"""
    collection_group_error_details: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_error_details.CollectionGroupErrorDetails"
    ]
    """<p>Error information for the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetCollectionGroupResponse) -> dict:
    out: dict = {}
    if "collection_group_details" in value:
        import aws_sdk_opensearchserverless.types.collection_group_details

        out["collectionGroupDetails"] = (
            aws_sdk_opensearchserverless.types.collection_group_details.serialize_aws_json_1_0(
                value["collection_group_details"]
            )
        )
    if "collection_group_error_details" in value:
        import aws_sdk_opensearchserverless.types.collection_group_error_details

        out["collectionGroupErrorDetails"] = (
            aws_sdk_opensearchserverless.types.collection_group_error_details.serialize_aws_json_1_0(
                value["collection_group_error_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetCollectionGroupResponse:
    out: BatchGetCollectionGroupResponse = {}  # type: ignore[typeddict-item]
    if "collectionGroupDetails" in data:
        import aws_sdk_opensearchserverless.types.collection_group_details

        out["collection_group_details"] = (
            aws_sdk_opensearchserverless.types.collection_group_details.deserialize_aws_json_1_0(
                data["collectionGroupDetails"]
            )
        )
    if "collectionGroupErrorDetails" in data:
        import aws_sdk_opensearchserverless.types.collection_group_error_details

        out["collection_group_error_details"] = (
            aws_sdk_opensearchserverless.types.collection_group_error_details.deserialize_aws_json_1_0(
                data["collectionGroupErrorDetails"]
            )
        )
    return out
