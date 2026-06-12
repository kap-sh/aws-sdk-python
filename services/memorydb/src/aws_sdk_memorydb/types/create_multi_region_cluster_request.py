"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateMultiRegionClusterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.boolean_optional
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.tag_list


class CreateMultiRegionClusterRequest(TypedDict):
    multi_region_cluster_name_suffix: "aws_sdk_memorydb.types.string.String"
    """<p>A suffix to be added to the Multi-Region cluster name. Amazon MemoryDB automatically applies a prefix to the Multi-Region cluster Name when it is created. Each Amazon Region has its own prefix. For instance, a Multi-Region cluster Name created in the US-West-1 region will begin with \"virxk\", along with the suffix name you provide. The suffix guarantees uniqueness of the Multi-Region cluster name across multiple regions.</p>"""
    description: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>A description for the multi-Region cluster.</p>"""
    engine: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the engine to be used for the multi-Region cluster.</p>"""
    engine_version: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The version of the engine to be used for the multi-Region cluster.</p>"""
    node_type: "aws_sdk_memorydb.types.string.String"
    """<p>The node type to be used for the multi-Region cluster.</p>"""
    multi_region_parameter_group_name: NotRequired[
        "aws_sdk_memorydb.types.string.String"
    ]
    """<p>The name of the multi-Region parameter group to be associated with the cluster.</p>"""
    num_shards: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The number of shards for the multi-Region cluster.</p>"""
    tls_enabled: NotRequired["aws_sdk_memorydb.types.boolean_optional.BooleanOptional"]
    """<p>Whether to enable TLS encryption for the multi-Region cluster.</p>"""
    tags: NotRequired["aws_sdk_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be applied to the multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMultiRegionClusterRequest) -> dict:
    out: dict = {}
    out["MultiRegionClusterNameSuffix"] = value["multi_region_cluster_name_suffix"]
    if "description" in value:
        out["Description"] = value["description"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    out["NodeType"] = value["node_type"]
    if "multi_region_parameter_group_name" in value:
        out["MultiRegionParameterGroupName"] = value[
            "multi_region_parameter_group_name"
        ]
    if "num_shards" in value:
        out["NumShards"] = value["num_shards"]
    if "tls_enabled" in value:
        out["TLSEnabled"] = value["tls_enabled"]
    if "tags" in value:
        import aws_sdk_memorydb.types.tag_list

        out["Tags"] = aws_sdk_memorydb.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMultiRegionClusterRequest:
    out: CreateMultiRegionClusterRequest = {}  # type: ignore[typeddict-item]
    if "MultiRegionClusterNameSuffix" in data:
        out["multi_region_cluster_name_suffix"] = data["MultiRegionClusterNameSuffix"]
    else:
        raise DeserializationError(
            "CreateMultiRegionClusterRequest.multi_region_cluster_name_suffix required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    else:
        raise DeserializationError("CreateMultiRegionClusterRequest.node_type required")
    if "MultiRegionParameterGroupName" in data:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    if "NumShards" in data:
        out["num_shards"] = data["NumShards"]
    if "TLSEnabled" in data:
        out["tls_enabled"] = data["TLSEnabled"]
    if "Tags" in data:
        import aws_sdk_memorydb.types.tag_list

        out["tags"] = aws_sdk_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
