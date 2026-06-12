"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetCollectionGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_ids
    import aws_sdk_opensearchserverless.types.collection_group_names


class BatchGetCollectionGroupRequest(TypedDict):
    ids: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_ids.CollectionGroupIds"
    ]
    """<p>A list of collection group IDs. You can't provide names and IDs in the same request.</p>"""
    names: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_names.CollectionGroupNames"
    ]
    """<p>A list of collection group names. You can't provide names and IDs in the same request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetCollectionGroupRequest) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_opensearchserverless.types.collection_group_ids

        out["ids"] = (
            aws_sdk_opensearchserverless.types.collection_group_ids.serialize_aws_json_1_0(
                value["ids"]
            )
        )
    if "names" in value:
        import aws_sdk_opensearchserverless.types.collection_group_names

        out["names"] = (
            aws_sdk_opensearchserverless.types.collection_group_names.serialize_aws_json_1_0(
                value["names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetCollectionGroupRequest:
    out: BatchGetCollectionGroupRequest = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_opensearchserverless.types.collection_group_ids

        out["ids"] = (
            aws_sdk_opensearchserverless.types.collection_group_ids.deserialize_aws_json_1_0(
                data["ids"]
            )
        )
    if "names" in data:
        import aws_sdk_opensearchserverless.types.collection_group_names

        out["names"] = (
            aws_sdk_opensearchserverless.types.collection_group_names.deserialize_aws_json_1_0(
                data["names"]
            )
        )
    return out
