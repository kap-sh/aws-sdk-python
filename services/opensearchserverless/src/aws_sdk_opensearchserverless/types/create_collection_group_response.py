"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateCollectionGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.create_collection_group_detail


class CreateCollectionGroupResponse(TypedDict):
    create_collection_group_detail: NotRequired[
        "aws_sdk_opensearchserverless.types.create_collection_group_detail.CreateCollectionGroupDetail"
    ]
    """<p>Details about the created collection group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCollectionGroupResponse) -> dict:
    out: dict = {}
    if "create_collection_group_detail" in value:
        import aws_sdk_opensearchserverless.types.create_collection_group_detail

        out["createCollectionGroupDetail"] = (
            aws_sdk_opensearchserverless.types.create_collection_group_detail.serialize_aws_json_1_0(
                value["create_collection_group_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCollectionGroupResponse:
    out: CreateCollectionGroupResponse = {}  # type: ignore[typeddict-item]
    if "createCollectionGroupDetail" in data:
        import aws_sdk_opensearchserverless.types.create_collection_group_detail

        out["create_collection_group_detail"] = (
            aws_sdk_opensearchserverless.types.create_collection_group_detail.deserialize_aws_json_1_0(
                data["createCollectionGroupDetail"]
            )
        )
    return out
