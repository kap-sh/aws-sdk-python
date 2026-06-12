"""Generated from Smithy shape ``com.amazonaws.opensearch#ClusterConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.cold_storage_options
    import aws_sdk_opensearch.types.integer_class
    import aws_sdk_opensearch.types.node_options_list
    import aws_sdk_opensearch.types.open_search_partition_instance_type
    import aws_sdk_opensearch.types.open_search_warm_partition_instance_type
    import aws_sdk_opensearch.types.zone_awareness_config


class ClusterConfig(TypedDict):
    instance_type: NotRequired[
        "aws_sdk_opensearch.types.open_search_partition_instance_type.OpenSearchPartitionInstanceType"
    ]
    """<p>Instance type of data nodes in the cluster.</p>"""
    instance_count: NotRequired["aws_sdk_opensearch.types.integer_class.IntegerClass"]
    """<p>Number of data nodes in the cluster. This number must be greater than 1, otherwise you receive a validation exception.</p>"""
    dedicated_master_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether dedicated master nodes are enabled for the cluster.<code>True</code> if the cluster will use a dedicated master node.<code>False</code> if the cluster will not.</p>"""
    zone_awareness_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether multiple Availability Zones are enabled. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html\">Configuring a multi-AZ domain in Amazon OpenSearch Service</a>.</p>"""
    zone_awareness_config: NotRequired[
        "aws_sdk_opensearch.types.zone_awareness_config.ZoneAwarenessConfig"
    ]
    """<p>Container for zone awareness configuration options. Only required if <code>ZoneAwarenessEnabled</code> is <code>true</code>.</p>"""
    dedicated_master_type: NotRequired[
        "aws_sdk_opensearch.types.open_search_partition_instance_type.OpenSearchPartitionInstanceType"
    ]
    """<p>OpenSearch Service instance type of the dedicated master nodes in the cluster.</p>"""
    dedicated_master_count: NotRequired[
        "aws_sdk_opensearch.types.integer_class.IntegerClass"
    ]
    """<p>Number of dedicated master nodes in the cluster. This number must be greater than 2 and not 4, otherwise you receive a validation exception.</p>"""
    warm_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether to enable warm storage for the cluster.</p>"""
    warm_type: NotRequired[
        "aws_sdk_opensearch.types.open_search_warm_partition_instance_type.OpenSearchWarmPartitionInstanceType"
    ]
    """<p>The instance type for the cluster's warm nodes.</p>"""
    warm_count: NotRequired["aws_sdk_opensearch.types.integer_class.IntegerClass"]
    """<p>The number of warm nodes in the cluster.</p>"""
    cold_storage_options: NotRequired[
        "aws_sdk_opensearch.types.cold_storage_options.ColdStorageOptions"
    ]
    """<p>Container for cold storage configuration options.</p>"""
    multi_az_with_standby_enabled: NotRequired[
        "aws_sdk_opensearch.types.boolean.Boolean"
    ]
    """<p>A boolean that indicates whether a multi-AZ domain is turned on with a standby AZ. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html\">Configuring a multi-AZ domain in Amazon OpenSearch Service</a>. </p>"""
    node_options: NotRequired[
        "aws_sdk_opensearch.types.node_options_list.NodeOptionsList"
    ]
    """<p>List of node options for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterConfig) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["InstanceType"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.serialize_json(
                value["instance_type"]
            )
        )
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "dedicated_master_enabled" in value:
        out["DedicatedMasterEnabled"] = value["dedicated_master_enabled"]
    if "zone_awareness_enabled" in value:
        out["ZoneAwarenessEnabled"] = value["zone_awareness_enabled"]
    if "zone_awareness_config" in value:
        import aws_sdk_opensearch.types.zone_awareness_config

        out["ZoneAwarenessConfig"] = (
            aws_sdk_opensearch.types.zone_awareness_config.serialize_json(
                value["zone_awareness_config"]
            )
        )
    if "dedicated_master_type" in value:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["DedicatedMasterType"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.serialize_json(
                value["dedicated_master_type"]
            )
        )
    if "dedicated_master_count" in value:
        out["DedicatedMasterCount"] = value["dedicated_master_count"]
    if "warm_enabled" in value:
        out["WarmEnabled"] = value["warm_enabled"]
    if "warm_type" in value:
        import aws_sdk_opensearch.types.open_search_warm_partition_instance_type

        out["WarmType"] = (
            aws_sdk_opensearch.types.open_search_warm_partition_instance_type.serialize_json(
                value["warm_type"]
            )
        )
    if "warm_count" in value:
        out["WarmCount"] = value["warm_count"]
    if "cold_storage_options" in value:
        import aws_sdk_opensearch.types.cold_storage_options

        out["ColdStorageOptions"] = (
            aws_sdk_opensearch.types.cold_storage_options.serialize_json(
                value["cold_storage_options"]
            )
        )
    if "multi_az_with_standby_enabled" in value:
        out["MultiAZWithStandbyEnabled"] = value["multi_az_with_standby_enabled"]
    if "node_options" in value:
        import aws_sdk_opensearch.types.node_options_list

        out["NodeOptions"] = aws_sdk_opensearch.types.node_options_list.serialize_json(
            value["node_options"]
        )
    return out


def deserialize_json(data: dict) -> ClusterConfig:
    out: ClusterConfig = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["instance_type"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.deserialize_json(
                data["InstanceType"]
            )
        )
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "DedicatedMasterEnabled" in data:
        out["dedicated_master_enabled"] = data["DedicatedMasterEnabled"]
    if "ZoneAwarenessEnabled" in data:
        out["zone_awareness_enabled"] = data["ZoneAwarenessEnabled"]
    if "ZoneAwarenessConfig" in data:
        import aws_sdk_opensearch.types.zone_awareness_config

        out["zone_awareness_config"] = (
            aws_sdk_opensearch.types.zone_awareness_config.deserialize_json(
                data["ZoneAwarenessConfig"]
            )
        )
    if "DedicatedMasterType" in data:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["dedicated_master_type"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.deserialize_json(
                data["DedicatedMasterType"]
            )
        )
    if "DedicatedMasterCount" in data:
        out["dedicated_master_count"] = data["DedicatedMasterCount"]
    if "WarmEnabled" in data:
        out["warm_enabled"] = data["WarmEnabled"]
    if "WarmType" in data:
        import aws_sdk_opensearch.types.open_search_warm_partition_instance_type

        out["warm_type"] = (
            aws_sdk_opensearch.types.open_search_warm_partition_instance_type.deserialize_json(
                data["WarmType"]
            )
        )
    if "WarmCount" in data:
        out["warm_count"] = data["WarmCount"]
    if "ColdStorageOptions" in data:
        import aws_sdk_opensearch.types.cold_storage_options

        out["cold_storage_options"] = (
            aws_sdk_opensearch.types.cold_storage_options.deserialize_json(
                data["ColdStorageOptions"]
            )
        )
    if "MultiAZWithStandbyEnabled" in data:
        out["multi_az_with_standby_enabled"] = data["MultiAZWithStandbyEnabled"]
    if "NodeOptions" in data:
        import aws_sdk_opensearch.types.node_options_list

        out["node_options"] = (
            aws_sdk_opensearch.types.node_options_list.deserialize_json(
                data["NodeOptions"]
            )
        )
    return out
