"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainHealthResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.domain_health
    import aws_sdk_opensearch.types.domain_state
    import aws_sdk_opensearch.types.environment_info_list
    import aws_sdk_opensearch.types.master_node_status
    import aws_sdk_opensearch.types.number_of_a_zs
    import aws_sdk_opensearch.types.number_of_nodes
    import aws_sdk_opensearch.types.number_of_shards


class DescribeDomainHealthResponse(TypedDict, closed=True):
    domain_state: NotRequired["aws_sdk_opensearch.types.domain_state.DomainState"]
    """<p>The current state of the domain.</p> <ul> <li> <p> <code>Processing</code> - The domain has updates in progress.</p> </li> <li> <p> <code>Active</code> - Requested changes have been processed and deployed to the domain.</p> </li> </ul>"""
    availability_zone_count: NotRequired[
        "aws_sdk_opensearch.types.number_of_a_zs.NumberOfAZs"
    ]
    """<p>The number of Availability Zones configured for the domain. If the service is unable to fetch this information, it will return <code>NotAvailable</code>.</p>"""
    active_availability_zone_count: NotRequired[
        "aws_sdk_opensearch.types.number_of_a_zs.NumberOfAZs"
    ]
    """<p>The number of active Availability Zones configured for the domain. If the service is unable to fetch this information, it will return <code>NotAvailable</code>.</p>"""
    stand_by_availability_zone_count: NotRequired[
        "aws_sdk_opensearch.types.number_of_a_zs.NumberOfAZs"
    ]
    """<p>The number of standby Availability Zones configured for the domain. If the service is unable to fetch this information, it will return <code>NotAvailable</code>.</p>"""
    data_node_count: NotRequired[
        "aws_sdk_opensearch.types.number_of_nodes.NumberOfNodes"
    ]
    """<p>The number of data nodes configured for the domain. If the service is unable to fetch this information, it will return <code>NotAvailable</code>.</p>"""
    dedicated_master: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>A boolean that indicates if dedicated master nodes are activated for the domain.</p>"""
    master_eligible_node_count: NotRequired[
        "aws_sdk_opensearch.types.number_of_nodes.NumberOfNodes"
    ]
    """<p>The number of nodes that can be elected as a master node. If dedicated master nodes is turned on, this value is the number of dedicated master nodes configured for the domain. If the service is unable to fetch this information, it will return <code>NotAvailable</code>.</p>"""
    warm_node_count: NotRequired[
        "aws_sdk_opensearch.types.number_of_nodes.NumberOfNodes"
    ]
    """<p>The number of warm nodes configured for the domain.</p>"""
    master_node: NotRequired[
        "aws_sdk_opensearch.types.master_node_status.MasterNodeStatus"
    ]
    """<p>Indicates whether the domain has an elected master node.</p> <ul> <li> <p> <b>Available</b> - The domain has an elected master node.</p> </li> <li> <p> <b>UnAvailable</b> - The master node hasn't yet been elected, and a quorum to elect a new master node hasn't been reached.</p> </li> </ul>"""
    cluster_health: NotRequired["aws_sdk_opensearch.types.domain_health.DomainHealth"]
    """<p>The current health status of your cluster.</p> <ul> <li> <p> <code>Red</code> - At least one primary shard is not allocated to any node.</p> </li> <li> <p> <code>Yellow</code> - All primary shards are allocated to nodes, but some replicas aren’t.</p> </li> <li> <p> <code>Green</code> - All primary shards and their replicas are allocated to nodes.</p> </li> <li> <p> <code>NotAvailable</code> - Unable to retrieve cluster health.</p> </li> </ul>"""
    total_shards: NotRequired[
        "aws_sdk_opensearch.types.number_of_shards.NumberOfShards"
    ]
    """<p>The total number of primary and replica shards for the domain.</p>"""
    total_un_assigned_shards: NotRequired[
        "aws_sdk_opensearch.types.number_of_shards.NumberOfShards"
    ]
    """<p>The total number of primary and replica shards not allocated to any of the nodes for the cluster.</p>"""
    environment_information: NotRequired[
        "aws_sdk_opensearch.types.environment_info_list.EnvironmentInfoList"
    ]
    """<p>A list of <code>EnvironmentInfo</code> for the domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainHealthResponse) -> dict:
    out: dict = {}
    if "domain_state" in value:
        import aws_sdk_opensearch.types.domain_state

        out["DomainState"] = aws_sdk_opensearch.types.domain_state.serialize_json(
            value["domain_state"]
        )
    if "availability_zone_count" in value:
        out["AvailabilityZoneCount"] = value["availability_zone_count"]
    if "active_availability_zone_count" in value:
        out["ActiveAvailabilityZoneCount"] = value["active_availability_zone_count"]
    if "stand_by_availability_zone_count" in value:
        out["StandByAvailabilityZoneCount"] = value["stand_by_availability_zone_count"]
    if "data_node_count" in value:
        out["DataNodeCount"] = value["data_node_count"]
    if "dedicated_master" in value:
        out["DedicatedMaster"] = value["dedicated_master"]
    if "master_eligible_node_count" in value:
        out["MasterEligibleNodeCount"] = value["master_eligible_node_count"]
    if "warm_node_count" in value:
        out["WarmNodeCount"] = value["warm_node_count"]
    if "master_node" in value:
        import aws_sdk_opensearch.types.master_node_status

        out["MasterNode"] = aws_sdk_opensearch.types.master_node_status.serialize_json(
            value["master_node"]
        )
    if "cluster_health" in value:
        import aws_sdk_opensearch.types.domain_health

        out["ClusterHealth"] = aws_sdk_opensearch.types.domain_health.serialize_json(
            value["cluster_health"]
        )
    if "total_shards" in value:
        out["TotalShards"] = value["total_shards"]
    if "total_un_assigned_shards" in value:
        out["TotalUnAssignedShards"] = value["total_un_assigned_shards"]
    if "environment_information" in value:
        import aws_sdk_opensearch.types.environment_info_list

        out["EnvironmentInformation"] = (
            aws_sdk_opensearch.types.environment_info_list.serialize_json(
                value["environment_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDomainHealthResponse:
    out: DescribeDomainHealthResponse = {}  # type: ignore[typeddict-item]
    if "DomainState" in data:
        import aws_sdk_opensearch.types.domain_state

        out["domain_state"] = aws_sdk_opensearch.types.domain_state.deserialize_json(
            data["DomainState"]
        )
    if "AvailabilityZoneCount" in data:
        out["availability_zone_count"] = data["AvailabilityZoneCount"]
    if "ActiveAvailabilityZoneCount" in data:
        out["active_availability_zone_count"] = data["ActiveAvailabilityZoneCount"]
    if "StandByAvailabilityZoneCount" in data:
        out["stand_by_availability_zone_count"] = data["StandByAvailabilityZoneCount"]
    if "DataNodeCount" in data:
        out["data_node_count"] = data["DataNodeCount"]
    if "DedicatedMaster" in data:
        out["dedicated_master"] = data["DedicatedMaster"]
    if "MasterEligibleNodeCount" in data:
        out["master_eligible_node_count"] = data["MasterEligibleNodeCount"]
    if "WarmNodeCount" in data:
        out["warm_node_count"] = data["WarmNodeCount"]
    if "MasterNode" in data:
        import aws_sdk_opensearch.types.master_node_status

        out["master_node"] = (
            aws_sdk_opensearch.types.master_node_status.deserialize_json(
                data["MasterNode"]
            )
        )
    if "ClusterHealth" in data:
        import aws_sdk_opensearch.types.domain_health

        out["cluster_health"] = aws_sdk_opensearch.types.domain_health.deserialize_json(
            data["ClusterHealth"]
        )
    if "TotalShards" in data:
        out["total_shards"] = data["TotalShards"]
    if "TotalUnAssignedShards" in data:
        out["total_un_assigned_shards"] = data["TotalUnAssignedShards"]
    if "EnvironmentInformation" in data:
        import aws_sdk_opensearch.types.environment_info_list

        out["environment_information"] = (
            aws_sdk_opensearch.types.environment_info_list.deserialize_json(
                data["EnvironmentInformation"]
            )
        )
    return out
