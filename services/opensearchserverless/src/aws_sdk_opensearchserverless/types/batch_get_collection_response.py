"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetCollectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_details
    import aws_sdk_opensearchserverless.types.collection_error_details


class BatchGetCollectionResponse(TypedDict, closed=True):
    collection_details: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_details.CollectionDetails"
    ]
    """<p>Details about each collection.</p>"""
    collection_error_details: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_error_details.CollectionErrorDetails"
    ]
    """<p>Error information for the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetCollectionResponse) -> dict:
    out: dict = {}
    if "collection_details" in value:
        import aws_sdk_opensearchserverless.types.collection_details

        out["collectionDetails"] = (
            aws_sdk_opensearchserverless.types.collection_details.serialize_aws_json_1_0(
                value["collection_details"]
            )
        )
    if "collection_error_details" in value:
        import aws_sdk_opensearchserverless.types.collection_error_details

        out["collectionErrorDetails"] = (
            aws_sdk_opensearchserverless.types.collection_error_details.serialize_aws_json_1_0(
                value["collection_error_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetCollectionResponse:
    out: BatchGetCollectionResponse = {}  # type: ignore[typeddict-item]
    if "collectionDetails" in data:
        import aws_sdk_opensearchserverless.types.collection_details

        out["collection_details"] = (
            aws_sdk_opensearchserverless.types.collection_details.deserialize_aws_json_1_0(
                data["collectionDetails"]
            )
        )
    if "collectionErrorDetails" in data:
        import aws_sdk_opensearchserverless.types.collection_error_details

        out["collection_error_details"] = (
            aws_sdk_opensearchserverless.types.collection_error_details.deserialize_aws_json_1_0(
                data["collectionErrorDetails"]
            )
        )
    return out
