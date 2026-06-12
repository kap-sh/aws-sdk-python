"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateCollectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.create_collection_detail


class CreateCollectionResponse(TypedDict):
    create_collection_detail: NotRequired[
        "aws_sdk_opensearchserverless.types.create_collection_detail.CreateCollectionDetail"
    ]
    """<p>Details about the collection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCollectionResponse) -> dict:
    out: dict = {}
    if "create_collection_detail" in value:
        import aws_sdk_opensearchserverless.types.create_collection_detail

        out["createCollectionDetail"] = (
            aws_sdk_opensearchserverless.types.create_collection_detail.serialize_aws_json_1_0(
                value["create_collection_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCollectionResponse:
    out: CreateCollectionResponse = {}  # type: ignore[typeddict-item]
    if "createCollectionDetail" in data:
        import aws_sdk_opensearchserverless.types.create_collection_detail

        out["create_collection_detail"] = (
            aws_sdk_opensearchserverless.types.create_collection_detail.deserialize_aws_json_1_0(
                data["createCollectionDetail"]
            )
        )
    return out
