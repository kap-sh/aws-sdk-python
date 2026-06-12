"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateCollectionGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.collection_group_capacity_limits
    import aws_sdk_opensearchserverless.types.collection_group_name
    import aws_sdk_opensearchserverless.types.serverless_generation
    import aws_sdk_opensearchserverless.types.standby_replicas
    import aws_sdk_opensearchserverless.types.tags


class CreateCollectionGroupRequest(TypedDict):
    name: "aws_sdk_opensearchserverless.types.collection_group_name.CollectionGroupName"
    """<p>The name of the collection group.</p>"""
    standby_replicas: (
        "aws_sdk_opensearchserverless.types.standby_replicas.StandbyReplicas"
    )
    """<p>Indicates whether standby replicas should be used for a collection group.</p>"""
    description: NotRequired["str"]
    """<p>A description of the collection group.</p>"""
    tags: NotRequired["aws_sdk_opensearchserverless.types.tags.Tags"]
    """<p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection group.</p>"""
    capacity_limits: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
    ]
    """<p>The capacity limits for the collection group, in OpenSearch Compute Units (OCUs). These limits control the maximum and minimum capacity for collections within the group.</p>"""
    generation: NotRequired[
        "aws_sdk_opensearchserverless.types.serverless_generation.ServerlessGeneration"
    ]
    """<p>The generation of Amazon OpenSearch Serverless for the collection group. Valid values are <code>CLASSIC</code> and <code>NEXTGEN</code>.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
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
        import aws_sdk_opensearchserverless.types.tags

        out["tags"] = aws_sdk_opensearchserverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "capacity_limits" in value:
        import aws_sdk_opensearchserverless.types.collection_group_capacity_limits

        out["capacityLimits"] = (
            aws_sdk_opensearchserverless.types.collection_group_capacity_limits.serialize_aws_json_1_0(
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
        import aws_sdk_opensearchserverless.types.tags

        out["tags"] = aws_sdk_opensearchserverless.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "capacityLimits" in data:
        import aws_sdk_opensearchserverless.types.collection_group_capacity_limits

        out["capacity_limits"] = (
            aws_sdk_opensearchserverless.types.collection_group_capacity_limits.deserialize_aws_json_1_0(
                data["capacityLimits"]
            )
        )
    if "generation" in data:
        out["generation"] = data["generation"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
