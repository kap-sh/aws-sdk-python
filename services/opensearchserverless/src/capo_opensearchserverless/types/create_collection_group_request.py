"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateCollectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_group_capacity_limits
    import capo_opensearchserverless.types.collection_group_name
    import capo_opensearchserverless.types.serverless_generation
    import capo_opensearchserverless.types.standby_replicas
    import capo_opensearchserverless.types.tags


class CreateCollectionGroupRequest(TypedDict, closed=True):
    name: "capo_opensearchserverless.types.collection_group_name.CollectionGroupName"
    """<p>The name of the collection group.</p>"""
    standby_replicas: "capo_opensearchserverless.types.standby_replicas.StandbyReplicas"
    """<p>Indicates whether standby replicas should be used for a collection group.</p>"""
    description: NotRequired["str"]
    """<p>A description of the collection group.</p>"""
    tags: NotRequired["capo_opensearchserverless.types.tags.Tags"]
    """<p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection group.</p>"""
    capacity_limits: NotRequired[
        "capo_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
    ]
    """<p>The capacity limits for the collection group, in OpenSearch Compute Units (OCUs). These limits control the maximum and minimum capacity for collections within the group.</p>"""
    generation: NotRequired[
        "capo_opensearchserverless.types.serverless_generation.ServerlessGeneration"
    ]
    """<p>The generation of Amazon OpenSearch Serverless for the collection group. Valid values are <code>CLASSIC</code> and <code>NEXTGEN</code>.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCollectionGroupRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["standbyReplicas"] = value["standby_replicas"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "capacity_limits" in value:
        import capo_opensearchserverless.types.collection_group_capacity_limits

        out["capacityLimits"] = (
            capo_opensearchserverless.types.collection_group_capacity_limits.serialize_aws_json_1_0(
                value["capacity_limits"]
            )
        )
    if "generation" in value:
        out["generation"] = value["generation"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCollectionGroupRequest:
    out: CreateCollectionGroupRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCollectionGroupRequest.name required")
    if "standbyReplicas" in data:
        out["standby_replicas"] = data["standbyReplicas"]
    else:
        raise DeserializationError(
            "CreateCollectionGroupRequest.standby_replicas required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "capacityLimits" in data:
        import capo_opensearchserverless.types.collection_group_capacity_limits

        out["capacity_limits"] = (
            capo_opensearchserverless.types.collection_group_capacity_limits.deserialize_aws_json_1_0(
                data["capacityLimits"]
            )
        )
    if "generation" in data:
        out["generation"] = data["generation"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
