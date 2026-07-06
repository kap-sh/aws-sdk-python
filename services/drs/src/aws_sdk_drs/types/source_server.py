"""Generated from Smithy shape ``com.amazonaws.drs#SourceServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.agent_version
    import aws_sdk_drs.types.arn
    import aws_sdk_drs.types.data_replication_info
    import aws_sdk_drs.types.last_launch_result
    import aws_sdk_drs.types.life_cycle
    import aws_sdk_drs.types.recovery_instance_id
    import aws_sdk_drs.types.replication_direction
    import aws_sdk_drs.types.source_cloud_properties
    import aws_sdk_drs.types.source_network_id
    import aws_sdk_drs.types.source_properties
    import aws_sdk_drs.types.source_server_arn
    import aws_sdk_drs.types.source_server_id
    import aws_sdk_drs.types.staging_area
    import aws_sdk_drs.types.tags_map


class SourceServer(TypedDict, closed=True):
    source_server_id: NotRequired["aws_sdk_drs.types.source_server_id.SourceServerID"]
    """<p>The ID of the Source Server.</p>"""
    arn: NotRequired["aws_sdk_drs.types.arn.ARN"]
    """<p>The ARN of the Source Server.</p>"""
    tags: NotRequired["aws_sdk_drs.types.tags_map.TagsMap"]
    """<p>The tags associated with the Source Server.</p>"""
    recovery_instance_id: NotRequired[
        "aws_sdk_drs.types.recovery_instance_id.RecoveryInstanceID"
    ]
    """<p>The ID of the Recovery Instance associated with this Source Server.</p>"""
    last_launch_result: NotRequired[
        "aws_sdk_drs.types.last_launch_result.LastLaunchResult"
    ]
    """<p>The status of the last recovery launch of this Source Server.</p>"""
    data_replication_info: NotRequired[
        "aws_sdk_drs.types.data_replication_info.DataReplicationInfo"
    ]
    """<p>The Data Replication Info of the Source Server.</p>"""
    life_cycle: NotRequired["aws_sdk_drs.types.life_cycle.LifeCycle"]
    """<p>The lifecycle information of this Source Server.</p>"""
    source_properties: NotRequired[
        "aws_sdk_drs.types.source_properties.SourceProperties"
    ]
    """<p>The source properties of the Source Server.</p>"""
    staging_area: NotRequired["aws_sdk_drs.types.staging_area.StagingArea"]
    """<p>The staging area of the source server.</p>"""
    source_cloud_properties: NotRequired[
        "aws_sdk_drs.types.source_cloud_properties.SourceCloudProperties"
    ]
    """<p>Source cloud properties of the Source Server.</p>"""
    replication_direction: NotRequired[
        "aws_sdk_drs.types.replication_direction.ReplicationDirection"
    ]
    """<p>Replication direction of the Source Server.</p>"""
    reversed_direction_source_server_arn: NotRequired[
        "aws_sdk_drs.types.source_server_arn.SourceServerARN"
    ]
    """<p>For EC2-originated Source Servers which have been failed over and then failed back, this value will mean the ARN of the Source Server on the opposite replication direction.</p>"""
    source_network_id: NotRequired[
        "aws_sdk_drs.types.source_network_id.SourceNetworkID"
    ]
    """<p>ID of the Source Network which is protecting this Source Server's network.</p>"""
    agent_version: NotRequired["aws_sdk_drs.types.agent_version.AgentVersion"]
    """<p>The version of the DRS agent installed on the source server</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceServer) -> dict:
    out: dict = {}
    if "source_server_id" in value:
        out["sourceServerID"] = value["source_server_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.serialize_json(value["tags"])
    if "recovery_instance_id" in value:
        out["recoveryInstanceId"] = value["recovery_instance_id"]
    if "last_launch_result" in value:
        out["lastLaunchResult"] = value["last_launch_result"]
    if "data_replication_info" in value:
        import aws_sdk_drs.types.data_replication_info

        out["dataReplicationInfo"] = (
            aws_sdk_drs.types.data_replication_info.serialize_json(
                value["data_replication_info"]
            )
        )
    if "life_cycle" in value:
        import aws_sdk_drs.types.life_cycle

        out["lifeCycle"] = aws_sdk_drs.types.life_cycle.serialize_json(
            value["life_cycle"]
        )
    if "source_properties" in value:
        import aws_sdk_drs.types.source_properties

        out["sourceProperties"] = aws_sdk_drs.types.source_properties.serialize_json(
            value["source_properties"]
        )
    if "staging_area" in value:
        import aws_sdk_drs.types.staging_area

        out["stagingArea"] = aws_sdk_drs.types.staging_area.serialize_json(
            value["staging_area"]
        )
    if "source_cloud_properties" in value:
        import aws_sdk_drs.types.source_cloud_properties

        out["sourceCloudProperties"] = (
            aws_sdk_drs.types.source_cloud_properties.serialize_json(
                value["source_cloud_properties"]
            )
        )
    if "replication_direction" in value:
        out["replicationDirection"] = value["replication_direction"]
    if "reversed_direction_source_server_arn" in value:
        out["reversedDirectionSourceServerArn"] = value[
            "reversed_direction_source_server_arn"
        ]
    if "source_network_id" in value:
        out["sourceNetworkID"] = value["source_network_id"]
    if "agent_version" in value:
        out["agentVersion"] = value["agent_version"]
    return out


def deserialize_json(data: dict) -> SourceServer:
    out: SourceServer = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.deserialize_json(data["tags"])
    if "recoveryInstanceId" in data:
        out["recovery_instance_id"] = data["recoveryInstanceId"]
    if "lastLaunchResult" in data:
        out["last_launch_result"] = data["lastLaunchResult"]
    if "dataReplicationInfo" in data:
        import aws_sdk_drs.types.data_replication_info

        out["data_replication_info"] = (
            aws_sdk_drs.types.data_replication_info.deserialize_json(
                data["dataReplicationInfo"]
            )
        )
    if "lifeCycle" in data:
        import aws_sdk_drs.types.life_cycle

        out["life_cycle"] = aws_sdk_drs.types.life_cycle.deserialize_json(
            data["lifeCycle"]
        )
    if "sourceProperties" in data:
        import aws_sdk_drs.types.source_properties

        out["source_properties"] = aws_sdk_drs.types.source_properties.deserialize_json(
            data["sourceProperties"]
        )
    if "stagingArea" in data:
        import aws_sdk_drs.types.staging_area

        out["staging_area"] = aws_sdk_drs.types.staging_area.deserialize_json(
            data["stagingArea"]
        )
    if "sourceCloudProperties" in data:
        import aws_sdk_drs.types.source_cloud_properties

        out["source_cloud_properties"] = (
            aws_sdk_drs.types.source_cloud_properties.deserialize_json(
                data["sourceCloudProperties"]
            )
        )
    if "replicationDirection" in data:
        out["replication_direction"] = data["replicationDirection"]
    if "reversedDirectionSourceServerArn" in data:
        out["reversed_direction_source_server_arn"] = data[
            "reversedDirectionSourceServerArn"
        ]
    if "sourceNetworkID" in data:
        out["source_network_id"] = data["sourceNetworkID"]
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    return out
