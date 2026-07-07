"""Generated from Smithy shape ``com.amazonaws.odb#DbSystemShapeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.compute_model
    import aws_sdk_odb.types.shape_type


class DbSystemShapeSummary(TypedDict, closed=True):
    available_core_count: NotRequired["int"]
    """<p>The maximum number of CPU cores that can be enabled for the shape.</p>"""
    available_core_count_per_node: NotRequired["int"]
    """<p>The maximum number of CPU cores per DB node that can be enabled for the shape.</p>"""
    available_data_storage_in_t_bs: NotRequired["int"]
    """<p>The maximum amount of data storage, in terabytes (TB), that can be enabled for the shape.</p>"""
    available_data_storage_per_server_in_t_bs: NotRequired["int"]
    """<p>The maximum amount of data storage, in terabytes (TB), that's available per storage server for the shape.</p>"""
    available_db_node_per_node_in_g_bs: NotRequired["int"]
    """<p>The maximum amount of DB node storage, in gigabytes (GB), that's available per DB node for the shape.</p>"""
    available_db_node_storage_in_g_bs: NotRequired["int"]
    """<p>The maximum amount of DB node storage, in gigabytes (GB), that can be enabled for the shape.</p>"""
    available_memory_in_g_bs: NotRequired["int"]
    """<p>The maximum amount of memory, in gigabytes (GB), that can be enabled for the shape.</p>"""
    available_memory_per_node_in_g_bs: NotRequired["int"]
    """<p>The maximum amount of memory, in gigabytes (GB), that's available per DB node for the shape.</p>"""
    core_count_increment: NotRequired["int"]
    """<p>The discrete number by which the CPU core count for the shape can be increased or decreased.</p>"""
    max_storage_count: NotRequired["int"]
    """<p>The maximum number of Exadata storage servers that's available for the shape.</p>"""
    maximum_node_count: NotRequired["int"]
    """<p>The maximum number of compute servers that is available for the shape.</p>"""
    min_core_count_per_node: NotRequired["int"]
    """<p>The minimum number of CPU cores that can be enabled per node for the shape.</p>"""
    min_data_storage_in_t_bs: NotRequired["int"]
    """<p>The minimum amount of data storage, in terabytes (TB), that must be allocated for the shape.</p>"""
    min_db_node_storage_per_node_in_g_bs: NotRequired["int"]
    """<p>The minimum amount of DB node storage, in gigabytes (GB), that must be allocated per DB node for the shape.</p>"""
    min_memory_per_node_in_g_bs: NotRequired["int"]
    """<p>The minimum amount of memory, in gigabytes (GB), that must be allocated per DB node for the shape.</p>"""
    min_storage_count: NotRequired["int"]
    """<p>The minimum number of Exadata storage servers that are available for the shape.</p>"""
    minimum_core_count: NotRequired["int"]
    """<p>The minimum number of CPU cores that can be enabled for the shape.</p>"""
    minimum_node_count: NotRequired["int"]
    """<p>The minimum number of compute servers that are available for the shape.</p>"""
    runtime_minimum_core_count: NotRequired["int"]
    """<p>The runtime minimum number of CPU cores that can be enabled for the shape.</p>"""
    shape_family: NotRequired["str"]
    """<p>The family of the shape.</p>"""
    shape_type: NotRequired["aws_sdk_odb.types.shape_type.ShapeType"]
    """<p>The shape type. This property is determined by the CPU hardware.</p>"""
    name: NotRequired["str"]
    """<p>The name of the shape.</p>"""
    compute_model: NotRequired["aws_sdk_odb.types.compute_model.ComputeModel"]
    """<p>The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled. </p>"""
    are_server_types_supported: NotRequired["bool"]
    """<p>Indicates whether the hardware system model supports configurable database and server storage types.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbSystemShapeSummary) -> dict:
    out: dict = {}
    if "available_core_count" in value:
        out["availableCoreCount"] = value["available_core_count"]
    if "available_core_count_per_node" in value:
        out["availableCoreCountPerNode"] = value["available_core_count_per_node"]
    if "available_data_storage_in_t_bs" in value:
        out["availableDataStorageInTBs"] = value["available_data_storage_in_t_bs"]
    if "available_data_storage_per_server_in_t_bs" in value:
        out["availableDataStoragePerServerInTBs"] = value[
            "available_data_storage_per_server_in_t_bs"
        ]
    if "available_db_node_per_node_in_g_bs" in value:
        out["availableDbNodePerNodeInGBs"] = value["available_db_node_per_node_in_g_bs"]
    if "available_db_node_storage_in_g_bs" in value:
        out["availableDbNodeStorageInGBs"] = value["available_db_node_storage_in_g_bs"]
    if "available_memory_in_g_bs" in value:
        out["availableMemoryInGBs"] = value["available_memory_in_g_bs"]
    if "available_memory_per_node_in_g_bs" in value:
        out["availableMemoryPerNodeInGBs"] = value["available_memory_per_node_in_g_bs"]
    if "core_count_increment" in value:
        out["coreCountIncrement"] = value["core_count_increment"]
    if "max_storage_count" in value:
        out["maxStorageCount"] = value["max_storage_count"]
    if "maximum_node_count" in value:
        out["maximumNodeCount"] = value["maximum_node_count"]
    if "min_core_count_per_node" in value:
        out["minCoreCountPerNode"] = value["min_core_count_per_node"]
    if "min_data_storage_in_t_bs" in value:
        out["minDataStorageInTBs"] = value["min_data_storage_in_t_bs"]
    if "min_db_node_storage_per_node_in_g_bs" in value:
        out["minDbNodeStoragePerNodeInGBs"] = value[
            "min_db_node_storage_per_node_in_g_bs"
        ]
    if "min_memory_per_node_in_g_bs" in value:
        out["minMemoryPerNodeInGBs"] = value["min_memory_per_node_in_g_bs"]
    if "min_storage_count" in value:
        out["minStorageCount"] = value["min_storage_count"]
    if "minimum_core_count" in value:
        out["minimumCoreCount"] = value["minimum_core_count"]
    if "minimum_node_count" in value:
        out["minimumNodeCount"] = value["minimum_node_count"]
    if "runtime_minimum_core_count" in value:
        out["runtimeMinimumCoreCount"] = value["runtime_minimum_core_count"]
    if "shape_family" in value:
        out["shapeFamily"] = value["shape_family"]
    if "shape_type" in value:
        import aws_sdk_odb.types.shape_type

        out["shapeType"] = aws_sdk_odb.types.shape_type.serialize_aws_json_1_0(
            value["shape_type"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "compute_model" in value:
        import aws_sdk_odb.types.compute_model

        out["computeModel"] = aws_sdk_odb.types.compute_model.serialize_aws_json_1_0(
            value["compute_model"]
        )
    if "are_server_types_supported" in value:
        out["areServerTypesSupported"] = value["are_server_types_supported"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DbSystemShapeSummary:
    out: DbSystemShapeSummary = {}  # type: ignore[typeddict-item]
    if "availableCoreCount" in data:
        out["available_core_count"] = data["availableCoreCount"]
    if "availableCoreCountPerNode" in data:
        out["available_core_count_per_node"] = data["availableCoreCountPerNode"]
    if "availableDataStorageInTBs" in data:
        out["available_data_storage_in_t_bs"] = data["availableDataStorageInTBs"]
    if "availableDataStoragePerServerInTBs" in data:
        out["available_data_storage_per_server_in_t_bs"] = data[
            "availableDataStoragePerServerInTBs"
        ]
    if "availableDbNodePerNodeInGBs" in data:
        out["available_db_node_per_node_in_g_bs"] = data["availableDbNodePerNodeInGBs"]
    if "availableDbNodeStorageInGBs" in data:
        out["available_db_node_storage_in_g_bs"] = data["availableDbNodeStorageInGBs"]
    if "availableMemoryInGBs" in data:
        out["available_memory_in_g_bs"] = data["availableMemoryInGBs"]
    if "availableMemoryPerNodeInGBs" in data:
        out["available_memory_per_node_in_g_bs"] = data["availableMemoryPerNodeInGBs"]
    if "coreCountIncrement" in data:
        out["core_count_increment"] = data["coreCountIncrement"]
    if "maxStorageCount" in data:
        out["max_storage_count"] = data["maxStorageCount"]
    if "maximumNodeCount" in data:
        out["maximum_node_count"] = data["maximumNodeCount"]
    if "minCoreCountPerNode" in data:
        out["min_core_count_per_node"] = data["minCoreCountPerNode"]
    if "minDataStorageInTBs" in data:
        out["min_data_storage_in_t_bs"] = data["minDataStorageInTBs"]
    if "minDbNodeStoragePerNodeInGBs" in data:
        out["min_db_node_storage_per_node_in_g_bs"] = data[
            "minDbNodeStoragePerNodeInGBs"
        ]
    if "minMemoryPerNodeInGBs" in data:
        out["min_memory_per_node_in_g_bs"] = data["minMemoryPerNodeInGBs"]
    if "minStorageCount" in data:
        out["min_storage_count"] = data["minStorageCount"]
    if "minimumCoreCount" in data:
        out["minimum_core_count"] = data["minimumCoreCount"]
    if "minimumNodeCount" in data:
        out["minimum_node_count"] = data["minimumNodeCount"]
    if "runtimeMinimumCoreCount" in data:
        out["runtime_minimum_core_count"] = data["runtimeMinimumCoreCount"]
    if "shapeFamily" in data:
        out["shape_family"] = data["shapeFamily"]
    if "shapeType" in data:
        import aws_sdk_odb.types.shape_type

        out["shape_type"] = aws_sdk_odb.types.shape_type.deserialize_aws_json_1_0(
            data["shapeType"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "computeModel" in data:
        import aws_sdk_odb.types.compute_model

        out["compute_model"] = aws_sdk_odb.types.compute_model.deserialize_aws_json_1_0(
            data["computeModel"]
        )
    if "areServerTypesSupported" in data:
        out["are_server_types_supported"] = data["areServerTypesSupported"]
    return out
