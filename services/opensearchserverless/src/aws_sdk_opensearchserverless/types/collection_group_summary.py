"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_capacity_limits
    import aws_sdk_opensearchserverless.types.collection_group_id
    import aws_sdk_opensearchserverless.types.collection_group_name
    import aws_sdk_opensearchserverless.types.serverless_generation


class CollectionGroupSummary(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_id.CollectionGroupId"
    ]
    """<p>The unique identifier of the collection group.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the collection group.</p>"""
    name: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_name.CollectionGroupName"
    ]
    """<p>The name of the collection group.</p>"""
    number_of_collections: NotRequired["int"]
    """<p>The number of collections within the collection group.</p>"""
    created_date: NotRequired["int"]
    """<p>The Epoch time when the collection group was created.</p>"""
    capacity_limits: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
    ]
    generation: NotRequired[
        "aws_sdk_opensearchserverless.types.serverless_generation.ServerlessGeneration"
    ]
    """<p>The generation of Amazon OpenSearch Serverless for the collection group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionGroupSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "number_of_collections" in value:
        out["numberOfCollections"] = value["number_of_collections"]
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "capacity_limits" in value:
        import aws_sdk_opensearchserverless.types.collection_group_capacity_limits

        out["capacityLimits"] = (
            aws_sdk_opensearchserverless.types.collection_group_capacity_limits.serialize_aws_json_1_0(
                value["capacity_limits"]
            )
        )
    if "generation" in value:
        out["generation"] = value["generation"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CollectionGroupSummary:
    out: CollectionGroupSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "numberOfCollections" in data:
        out["number_of_collections"] = data["numberOfCollections"]
    if "createdDate" in data:
        out["created_date"] = data["createdDate"]
    if "capacityLimits" in data:
        import aws_sdk_opensearchserverless.types.collection_group_capacity_limits

        out["capacity_limits"] = (
            aws_sdk_opensearchserverless.types.collection_group_capacity_limits.deserialize_aws_json_1_0(
                data["capacityLimits"]
            )
        )
    if "generation" in data:
        out["generation"] = data["generation"]
    return out
