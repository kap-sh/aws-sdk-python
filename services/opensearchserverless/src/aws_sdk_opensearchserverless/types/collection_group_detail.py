"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionGroupDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_capacity_limits
    import aws_sdk_opensearchserverless.types.collection_group_id
    import aws_sdk_opensearchserverless.types.collection_group_name
    import aws_sdk_opensearchserverless.types.current_capacity
    import aws_sdk_opensearchserverless.types.serverless_generation
    import aws_sdk_opensearchserverless.types.standby_replicas
    import aws_sdk_opensearchserverless.types.tags


class CollectionGroupDetail(TypedDict):
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
    standby_replicas: NotRequired[
        "aws_sdk_opensearchserverless.types.standby_replicas.StandbyReplicas"
    ]
    """<p>Indicates whether standby replicas are used for the collection group.</p>"""
    description: NotRequired["str"]
    """<p>The description of the collection group.</p>"""
    tags: NotRequired["aws_sdk_opensearchserverless.types.tags.Tags"]
    """<p>A map of key-value pairs associated with the collection group.</p>"""
    created_date: NotRequired["int"]
    """<p>The Epoch time when the collection group was created.</p>"""
    capacity_limits: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
    ]
    """<p>The capacity limits for the collection group, in OpenSearch Compute Units (OCUs).</p>"""
    current_capacity: NotRequired[
        "aws_sdk_opensearchserverless.types.current_capacity.CurrentCapacity"
    ]
    """<p>Current search and indexing capacity for the collection group.</p>"""
    number_of_collections: NotRequired["int"]
    """<p>The number of collections associated with the collection group.</p>"""
    generation: NotRequired[
        "aws_sdk_opensearchserverless.types.serverless_generation.ServerlessGeneration"
    ]
    """<p>The generation of Amazon OpenSearch Serverless for the collection group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionGroupDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "standby_replicas" in value:
        out["standbyReplicas"] = value["standby_replicas"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_opensearchserverless.types.tags

        out["tags"] = aws_sdk_opensearchserverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "capacity_limits" in value:
        import aws_sdk_opensearchserverless.types.collection_group_capacity_limits

        out["capacityLimits"] = (
            aws_sdk_opensearchserverless.types.collection_group_capacity_limits.serialize_aws_json_1_0(
                value["capacity_limits"]
            )
        )
    if "current_capacity" in value:
        import aws_sdk_opensearchserverless.types.current_capacity

        out["currentCapacity"] = (
            aws_sdk_opensearchserverless.types.current_capacity.serialize_aws_json_1_0(
                value["current_capacity"]
            )
        )
    if "number_of_collections" in value:
        out["numberOfCollections"] = value["number_of_collections"]
    if "generation" in value:
        out["generation"] = value["generation"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CollectionGroupDetail:
    out: CollectionGroupDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "standbyReplicas" in data:
        out["standby_replicas"] = data["standbyReplicas"]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_opensearchserverless.types.tags

        out["tags"] = aws_sdk_opensearchserverless.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "createdDate" in data:
        out["created_date"] = data["createdDate"]
    if "capacityLimits" in data:
        import aws_sdk_opensearchserverless.types.collection_group_capacity_limits

        out["capacity_limits"] = (
            aws_sdk_opensearchserverless.types.collection_group_capacity_limits.deserialize_aws_json_1_0(
                data["capacityLimits"]
            )
        )
    if "currentCapacity" in data:
        import aws_sdk_opensearchserverless.types.current_capacity

        out["current_capacity"] = (
            aws_sdk_opensearchserverless.types.current_capacity.deserialize_aws_json_1_0(
                data["currentCapacity"]
            )
        )
    if "numberOfCollections" in data:
        out["number_of_collections"] = data["numberOfCollections"]
    if "generation" in data:
        out["generation"] = data["generation"]
    return out
