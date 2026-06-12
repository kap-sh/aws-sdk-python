"""Generated from Smithy shape ``com.amazonaws.keyspaces#KeyspaceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.arn
    import aws_sdk_keyspaces.types.keyspace_name
    import aws_sdk_keyspaces.types.region_list
    import aws_sdk_keyspaces.types.rs


class KeyspaceSummary(TypedDict):
    keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace.</p>"""
    resource_arn: "aws_sdk_keyspaces.types.arn.ARN"
    """<p>The unique identifier of the keyspace in the format of an Amazon Resource Name (ARN).</p>"""
    replication_strategy: "aws_sdk_keyspaces.types.rs.rs"
    """<p> This property specifies if a keyspace is a single Region keyspace or a multi-Region keyspace. The available values are <code>SINGLE_REGION</code> or <code>MULTI_REGION</code>. </p>"""
    replication_regions: NotRequired["aws_sdk_keyspaces.types.region_list.RegionList"]
    """<p> If the <code>replicationStrategy</code> of the keyspace is <code>MULTI_REGION</code>, a list of replication Regions is returned. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyspaceSummary) -> dict:
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
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyspaceSummary:
    out: KeyspaceSummary = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("KeyspaceSummary.keyspace_name required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("KeyspaceSummary.resource_arn required")
    if "replicationStrategy" in data:
        out["replication_strategy"] = data["replicationStrategy"]
    else:
        raise DeserializationError("KeyspaceSummary.replication_strategy required")
    if "replicationRegions" in data:
        import aws_sdk_keyspaces.types.region_list

        out["replication_regions"] = (
            aws_sdk_keyspaces.types.region_list.deserialize_aws_json_1_0(
                data["replicationRegions"]
            )
        )
    return out
