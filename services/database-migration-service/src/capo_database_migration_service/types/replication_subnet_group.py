"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationSubnetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.string_list
    import capo_database_migration_service.types.subnet_list


class ReplicationSubnetGroup(TypedDict, closed=True):
    replication_subnet_group_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The identifier of the replication instance subnet group.</p>"""
    replication_subnet_group_description: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A description for the replication subnet group.</p>"""
    vpc_id: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    subnet_group_status: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The status of the subnet group.</p>"""
    subnets: NotRequired["capo_database_migration_service.types.subnet_list.SubnetList"]
    """<p>The subnets that are in the subnet group.</p>"""
    supported_network_types: NotRequired[
        "capo_database_migration_service.types.string_list.StringList"
    ]
    """<p>The IP addressing protocol supported by the subnet group. This is used by a replication instance with values such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.</p>"""
    is_read_only: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the replication subnet group is read-only. When set to <code>true</code>, this subnet group is managed by DMS as part of a zero-ETL integration and cannot be modified or deleted directly. You can only modify or delete read-only subnet groups through their associated zero-ETL integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationSubnetGroup) -> dict:
    out: dict = {}
    if "replication_subnet_group_identifier" in value:
        out["ReplicationSubnetGroupIdentifier"] = value[
            "replication_subnet_group_identifier"
        ]
    if "replication_subnet_group_description" in value:
        out["ReplicationSubnetGroupDescription"] = value[
            "replication_subnet_group_description"
        ]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_group_status" in value:
        out["SubnetGroupStatus"] = value["subnet_group_status"]
    if "subnets" in value:
        import capo_database_migration_service.types.subnet_list

        out["Subnets"] = (
            capo_database_migration_service.types.subnet_list.serialize_aws_json_1_1(
                value["subnets"]
            )
        )
    if "supported_network_types" in value:
        import capo_database_migration_service.types.string_list

        out["SupportedNetworkTypes"] = (
            capo_database_migration_service.types.string_list.serialize_aws_json_1_1(
                value["supported_network_types"]
            )
        )
    if "is_read_only" in value:
        out["IsReadOnly"] = value["is_read_only"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationSubnetGroup:
    out: ReplicationSubnetGroup = {}  # type: ignore[typeddict-item]
    if "ReplicationSubnetGroupIdentifier" in data:
        out["replication_subnet_group_identifier"] = data[
            "ReplicationSubnetGroupIdentifier"
        ]
    if "ReplicationSubnetGroupDescription" in data:
        out["replication_subnet_group_description"] = data[
            "ReplicationSubnetGroupDescription"
        ]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SubnetGroupStatus" in data:
        out["subnet_group_status"] = data["SubnetGroupStatus"]
    if "Subnets" in data:
        import capo_database_migration_service.types.subnet_list

        out["subnets"] = (
            capo_database_migration_service.types.subnet_list.deserialize_aws_json_1_1(
                data["Subnets"]
            )
        )
    if "SupportedNetworkTypes" in data:
        import capo_database_migration_service.types.string_list

        out["supported_network_types"] = (
            capo_database_migration_service.types.string_list.deserialize_aws_json_1_1(
                data["SupportedNetworkTypes"]
            )
        )
    if "IsReadOnly" in data:
        out["is_read_only"] = data["IsReadOnly"]
    return out
