"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteCollectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.delete_collection_detail


class DeleteCollectionResponse(TypedDict, closed=True):
    delete_collection_detail: NotRequired[
        "aws_sdk_opensearchserverless.types.delete_collection_detail.DeleteCollectionDetail"
    ]
    """<p>Details of the deleted collection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteCollectionResponse) -> dict:
    out: dict = {}
    if "delete_collection_detail" in value:
        import aws_sdk_opensearchserverless.types.delete_collection_detail

        out["deleteCollectionDetail"] = (
            aws_sdk_opensearchserverless.types.delete_collection_detail.serialize_aws_json_1_0(
                value["delete_collection_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteCollectionResponse:
    out: DeleteCollectionResponse = {}  # type: ignore[typeddict-item]
    if "deleteCollectionDetail" in data:
        import aws_sdk_opensearchserverless.types.delete_collection_detail

        out["delete_collection_detail"] = (
            aws_sdk_opensearchserverless.types.delete_collection_detail.deserialize_aws_json_1_0(
                data["deleteCollectionDetail"]
            )
        )
    return out
