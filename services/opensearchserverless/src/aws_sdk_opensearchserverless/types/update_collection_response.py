"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateCollectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.update_collection_detail


class UpdateCollectionResponse(TypedDict, closed=True):
    update_collection_detail: NotRequired[
        "aws_sdk_opensearchserverless.types.update_collection_detail.UpdateCollectionDetail"
    ]
    """<p>Details about the updated collection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCollectionResponse) -> dict:
    out: dict = {}
    if "update_collection_detail" in value:
        import aws_sdk_opensearchserverless.types.update_collection_detail

        out["updateCollectionDetail"] = (
            aws_sdk_opensearchserverless.types.update_collection_detail.serialize_aws_json_1_0(
                value["update_collection_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCollectionResponse:
    out: UpdateCollectionResponse = {}  # type: ignore[typeddict-item]
    if "updateCollectionDetail" in data:
        import aws_sdk_opensearchserverless.types.update_collection_detail

        out["update_collection_detail"] = (
            aws_sdk_opensearchserverless.types.update_collection_detail.deserialize_aws_json_1_0(
                data["updateCollectionDetail"]
            )
        )
    return out
