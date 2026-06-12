"""Generated from Smithy shape ``com.amazonaws.keyspaces#GetKeyspaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.arn
    import aws_sdk_keyspaces.types.keyspace_name
    import aws_sdk_keyspaces.types.region_list
    import aws_sdk_keyspaces.types.replication_group_status_list
    import aws_sdk_keyspaces.types.rs


class GetKeyspaceResponse(TypedDict):
    keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace.</p>"""
    resource_arn: "aws_sdk_keyspaces.types.arn.ARN"
    """<p>Returns the ARN of the keyspace.</p>"""
    replication_strategy: "aws_sdk_keyspaces.types.rs.rs"
    """<p> Returns the replication strategy of the keyspace. The options are <code>SINGLE_REGION</code> or <code>MULTI_REGION</code>. </p>"""
    replication_regions: NotRequired["aws_sdk_keyspaces.types.region_list.RegionList"]
    """<p> If the <code>replicationStrategy</code> of the keyspace is <code>MULTI_REGION</code>, a list of replication Regions is returned. </p>"""
    replication_group_statuses: NotRequired[
        "aws_sdk_keyspaces.types.replication_group_status_list.ReplicationGroupStatusList"
    ]
    """<p> A list of all Regions the keyspace is replicated in after the update keyspace operation and their status. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetKeyspaceResponse) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["resourceArn"] = value["resource_arn"]
    out["replicationStrategy"] = value["replication_strategy"]
    if "replication_regions" in value:
        import aws_sdk_keyspaces.types.region_list

        out["replicationRegions"] = (
            aws_sdk_keyspaces.types.region_list.serialize_aws_json_1_0(
                value["replication_regions"]
            )
        )
    if "replication_group_statuses" in value:
        import aws_sdk_keyspaces.types.replication_group_status_list

        out["replicationGroupStatuses"] = (
            aws_sdk_keyspaces.types.replication_group_status_list.serialize_aws_json_1_0(
                value["replication_group_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetKeyspaceResponse:
    out: GetKeyspaceResponse = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("GetKeyspaceResponse.keyspace_name required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("GetKeyspaceResponse.resource_arn required")
    if "replicationStrategy" in data:
        out["replication_strategy"] = data["replicationStrategy"]
    else:
        raise DeserializationError("GetKeyspaceResponse.replication_strategy required")
    if "replicationRegions" in data:
        import aws_sdk_keyspaces.types.region_list

        out["replication_regions"] = (
            aws_sdk_keyspaces.types.region_list.deserialize_aws_json_1_0(
                data["replicationRegions"]
            )
        )
    if "replicationGroupStatuses" in data:
        import aws_sdk_keyspaces.types.replication_group_status_list

        out["replication_group_statuses"] = (
            aws_sdk_keyspaces.types.replication_group_status_list.deserialize_aws_json_1_0(
                data["replicationGroupStatuses"]
            )
        )
    return out
