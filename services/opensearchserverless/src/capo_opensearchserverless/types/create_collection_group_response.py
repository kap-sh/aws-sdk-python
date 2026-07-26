"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateCollectionGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.create_collection_group_detail


class CreateCollectionGroupResponse(TypedDict, closed=True):
    create_collection_group_detail: NotRequired[
        "capo_opensearchserverless.types.create_collection_group_detail.CreateCollectionGroupDetail"
    ]
    """<p>Details about the created collection group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCollectionGroupResponse) -> dict:
    out: dict = {}
    if "create_collection_group_detail" in value:
        import capo_opensearchserverless.types.create_collection_group_detail

        out["createCollectionGroupDetail"] = (
            capo_opensearchserverless.types.create_collection_group_detail.serialize_aws_json_1_0(
                value["create_collection_group_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCollectionGroupResponse:
    out: CreateCollectionGroupResponse = {}  # type: ignore[typeddict-item]
    if "createCollectionGroupDetail" in data:
        import capo_opensearchserverless.types.create_collection_group_detail

        out["create_collection_group_detail"] = (
            capo_opensearchserverless.types.create_collection_group_detail.deserialize_aws_json_1_0(
                data["createCollectionGroupDetail"]
            )
        )
    return out
