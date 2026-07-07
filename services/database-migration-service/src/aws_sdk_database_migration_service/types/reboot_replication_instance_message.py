"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RebootReplicationInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.string


class RebootReplicationInstanceMessage(TypedDict, closed=True):
    replication_instance_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the replication instance.</p>"""
    force_failover: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If this parameter is <code>true</code>, the reboot is conducted through a Multi-AZ failover. If the instance isn't configured for Multi-AZ, then you can't specify <code>true</code>. ( <code>--force-planned-failover</code> and <code>--force-failover</code> can't both be set to <code>true</code>.)</p>"""
    force_planned_failover: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If this parameter is <code>true</code>, the reboot is conducted through a planned Multi-AZ failover where resources are released and cleaned up prior to conducting the failover. If the instance isn''t configured for Multi-AZ, then you can't specify <code>true</code>. ( <code>--force-planned-failover</code> and <code>--force-failover</code> can't both be set to <code>true</code>.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebootReplicationInstanceMessage) -> dict:
    out: dict = {}
    out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    if "force_failover" in value:
        out["ForceFailover"] = value["force_failover"]
    if "force_planned_failover" in value:
        out["ForcePlannedFailover"] = value["force_planned_failover"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RebootReplicationInstanceMessage:
    out: RebootReplicationInstanceMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationInstanceArn" in data:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    else:
        raise DeserializationError(
            "RebootReplicationInstanceMessage.replication_instance_arn required"
        )
    if "ForceFailover" in data:
        out["force_failover"] = data["ForceFailover"]
    if "ForcePlannedFailover" in data:
        out["force_planned_failover"] = data["ForcePlannedFailover"]
    return out
