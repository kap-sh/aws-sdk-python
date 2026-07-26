"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetCollectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_group_ids
    import capo_opensearchserverless.types.collection_group_names


class BatchGetCollectionGroupRequest(TypedDict, closed=True):
    ids: NotRequired[
        "capo_opensearchserverless.types.collection_group_ids.CollectionGroupIds"
    ]
    """<p>A list of collection group IDs. You can't provide names and IDs in the same request.</p>"""
    names: NotRequired[
        "capo_opensearchserverless.types.collection_group_names.CollectionGroupNames"
    ]
    """<p>A list of collection group names. You can't provide names and IDs in the same request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetCollectionGroupRequest) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_opensearchserverless.types.collection_group_ids

        out["ids"] = (
            capo_opensearchserverless.types.collection_group_ids.serialize_aws_json_1_0(
                value["ids"]
            )
        )
    if "names" in value:
        import capo_opensearchserverless.types.collection_group_names

        out["names"] = (
            capo_opensearchserverless.types.collection_group_names.serialize_aws_json_1_0(
                value["names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetCollectionGroupRequest:
    out: BatchGetCollectionGroupRequest = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import capo_opensearchserverless.types.collection_group_ids

        out["ids"] = (
            capo_opensearchserverless.types.collection_group_ids.deserialize_aws_json_1_0(
                data["ids"]
            )
        )
    if "names" in data:
        import capo_opensearchserverless.types.collection_group_names

        out["names"] = (
            capo_opensearchserverless.types.collection_group_names.deserialize_aws_json_1_0(
                data["names"]
            )
        )
    return out
