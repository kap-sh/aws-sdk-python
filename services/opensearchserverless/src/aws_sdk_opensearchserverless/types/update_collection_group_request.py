"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateCollectionGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.collection_group_capacity_limits
    import aws_sdk_opensearchserverless.types.collection_group_id


class UpdateCollectionGroupRequest(TypedDict):
    id: "aws_sdk_opensearchserverless.types.collection_group_id.CollectionGroupId"
    """<p>The unique identifier of the collection group to update.</p>"""
    description: NotRequired["str"]
    """<p>A new description for the collection group.</p>"""
    capacity_limits: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
    ]
    """<p>Updated capacity limits for the collection group, in OpenSearch Compute Units (OCUs).</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCollectionGroupRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "capacity_limits" in value:
        import aws_sdk_opensearchserverless.types.collection_group_capacity_limits

        out["capacityLimits"] = (
            aws_sdk_opensearchserverless.types.collection_group_capacity_limits.serialize_aws_json_1_0(
                value["capacity_limits"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCollectionGroupRequest:
    out: UpdateCollectionGroupRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateCollectionGroupRequest.id required")
    if "description" in data:
        out["description"] = data["description"]
    if "capacityLimits" in data:
        import aws_sdk_opensearchserverless.types.collection_group_capacity_limits

        out["capacity_limits"] = (
            aws_sdk_opensearchserverless.types.collection_group_capacity_limits.deserialize_aws_json_1_0(
                data["capacityLimits"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
