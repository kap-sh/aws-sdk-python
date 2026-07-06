"""Generated from Smithy shape ``com.amazonaws.memorydb#MultiRegionCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.boolean_optional
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.regional_cluster_list
    import aws_sdk_memorydb.types.string


class MultiRegionCluster(TypedDict, closed=True):
    multi_region_cluster_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the multi-Region cluster.</p>"""
    description: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The description of the multi-Region cluster.</p>"""
    status: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The current status of the multi-Region cluster.</p>"""
    node_type: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The node type used by the multi-Region cluster.</p>"""
    engine: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the engine used by the multi-Region cluster.</p>"""
    engine_version: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The version of the engine used by the multi-Region cluster.</p>"""
    number_of_shards: NotRequired[
        "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of shards in the multi-Region cluster.</p>"""
    clusters: NotRequired[
        "aws_sdk_memorydb.types.regional_cluster_list.RegionalClusterList"
    ]
    """<p>The clusters in this multi-Region cluster.</p>"""
    multi_region_parameter_group_name: NotRequired[
        "aws_sdk_memorydb.types.string.String"
    ]
    """<p>The name of the multi-Region parameter group associated with the cluster.</p>"""
    tls_enabled: NotRequired["aws_sdk_memorydb.types.boolean_optional.BooleanOptional"]
    """<p>Indiciates if the multi-Region cluster is TLS enabled.</p>"""
    arn: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiRegionCluster) -> dict:
    out: dict = {}
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        out["Status"] = value["status"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "number_of_shards" in value:
        out["NumberOfShards"] = value["number_of_shards"]
    if "clusters" in value:
        import aws_sdk_memorydb.types.regional_cluster_list

        out["Clusters"] = (
            aws_sdk_memorydb.types.regional_cluster_list.serialize_aws_json_1_1(
                value["clusters"]
            )
        )
    if "multi_region_parameter_group_name" in value:
        out["MultiRegionParameterGroupName"] = value[
            "multi_region_parameter_group_name"
        ]
    if "tls_enabled" in value:
        out["TLSEnabled"] = value["tls_enabled"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MultiRegionCluster:
    out: MultiRegionCluster = {}  # type: ignore[typeddict-item]
    if "MultiRegionClusterName" in data:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "NumberOfShards" in data:
        out["number_of_shards"] = data["NumberOfShards"]
    if "Clusters" in data:
        import aws_sdk_memorydb.types.regional_cluster_list

        out["clusters"] = (
            aws_sdk_memorydb.types.regional_cluster_list.deserialize_aws_json_1_1(
                data["Clusters"]
            )
        )
    if "MultiRegionParameterGroupName" in data:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    if "TLSEnabled" in data:
        out["tls_enabled"] = data["TLSEnabled"]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    return out
