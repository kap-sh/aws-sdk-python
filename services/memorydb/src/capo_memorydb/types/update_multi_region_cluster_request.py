"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateMultiRegionClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_memorydb.types.shard_configuration_request
    import capo_memorydb.types.string
    import capo_memorydb.types.update_strategy


class UpdateMultiRegionClusterRequest(TypedDict, closed=True):
    multi_region_cluster_name: "capo_memorydb.types.string.String"
    """<p>The name of the multi-Region cluster to be updated.</p>"""
    node_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The new node type to be used for the multi-Region cluster.</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>A new description for the multi-Region cluster.</p>"""
    engine_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The new engine version to be used for the multi-Region cluster.</p>"""
    shard_configuration: NotRequired[
        "capo_memorydb.types.shard_configuration_request.ShardConfigurationRequest"
    ]
    multi_region_parameter_group_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The new multi-Region parameter group to be associated with the cluster.</p>"""
    update_strategy: NotRequired["capo_memorydb.types.update_strategy.UpdateStrategy"]
    r"""<p>The strategy to use for the update operation. Supported values are \"coordinated\" or \"uncoordinated\".</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMultiRegionClusterRequest) -> dict:
    out: dict = {}
    out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "description" in value:
        out["Description"] = value["description"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "shard_configuration" in value:
        import capo_memorydb.types.shard_configuration_request

        out["ShardConfiguration"] = (
            capo_memorydb.types.shard_configuration_request.serialize_aws_json_1_1(
                value["shard_configuration"]
            )
        )
    if "multi_region_parameter_group_name" in value:
        out["MultiRegionParameterGroupName"] = value[
            "multi_region_parameter_group_name"
        ]
    if "update_strategy" in value:
        import capo_memorydb.types.update_strategy

        out["UpdateStrategy"] = (
            capo_memorydb.types.update_strategy.serialize_aws_json_1_1(
                value["update_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMultiRegionClusterRequest:
    out: UpdateMultiRegionClusterRequest = {}  # type: ignore[typeddict-item]
    if "MultiRegionClusterName" in data:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    else:
        raise DeserializationError(
            "UpdateMultiRegionClusterRequest.multi_region_cluster_name required"
        )
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "ShardConfiguration" in data:
        import capo_memorydb.types.shard_configuration_request

        out["shard_configuration"] = (
            capo_memorydb.types.shard_configuration_request.deserialize_aws_json_1_1(
                data["ShardConfiguration"]
            )
        )
    if "MultiRegionParameterGroupName" in data:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    if "UpdateStrategy" in data:
        import capo_memorydb.types.update_strategy

        out["update_strategy"] = (
            capo_memorydb.types.update_strategy.deserialize_aws_json_1_1(
                data["UpdateStrategy"]
            )
        )
    return out
