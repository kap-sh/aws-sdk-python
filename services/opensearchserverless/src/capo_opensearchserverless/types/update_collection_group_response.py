"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateCollectionGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.update_collection_group_detail


class UpdateCollectionGroupResponse(TypedDict, closed=True):
    update_collection_group_detail: NotRequired[
        "capo_opensearchserverless.types.update_collection_group_detail.UpdateCollectionGroupDetail"
    ]
    """<p>Details about the updated collection group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCollectionGroupResponse) -> dict:
    out: dict = {}
    if "update_collection_group_detail" in value:
        import capo_opensearchserverless.types.update_collection_group_detail

        out["updateCollectionGroupDetail"] = (
            capo_opensearchserverless.types.update_collection_group_detail.serialize_aws_json_1_0(
                value["update_collection_group_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCollectionGroupResponse:
    out: UpdateCollectionGroupResponse = {}  # type: ignore[typeddict-item]
    if "updateCollectionGroupDetail" in data:
        import capo_opensearchserverless.types.update_collection_group_detail

        out["update_collection_group_detail"] = (
            capo_opensearchserverless.types.update_collection_group_detail.deserialize_aws_json_1_0(
                data["updateCollectionGroupDetail"]
            )
        )
    return out
