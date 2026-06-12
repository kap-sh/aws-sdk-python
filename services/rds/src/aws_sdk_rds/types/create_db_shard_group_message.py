"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBShardGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean_optional
    import aws_sdk_rds.types.double_optional
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.tag_list


class CreateDBShardGroupMessage(TypedDict):
    db_shard_group_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the DB shard group.</p>"""
    db_cluster_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the primary DB cluster for the DB shard group.</p>"""
    compute_redundancy: NotRequired[
        "aws_sdk_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies whether to create standby standby DB data access shard for the DB shard group. Valid values are the following:</p> <ul> <li> <p>0 - Creates a DB shard group without a standby DB data access shard. This is the default value.</p> </li> <li> <p>1 - Creates a DB shard group with a standby DB data access shard in a different Availability Zone (AZ).</p> </li> <li> <p>2 - Creates a DB shard group with two standby DB data access shard in two different AZs.</p> </li> </ul>"""
    max_acu: NotRequired["aws_sdk_rds.types.double_optional.DoubleOptional"]
    """<p>The maximum capacity of the DB shard group in Aurora capacity units (ACUs).</p>"""
    min_acu: NotRequired["aws_sdk_rds.types.double_optional.DoubleOptional"]
    """<p>The minimum capacity of the DB shard group in Aurora capacity units (ACUs).</p>"""
    publicly_accessible: NotRequired[
        "aws_sdk_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether the DB shard group is publicly accessible.</p> <p>When the DB shard group is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB shard group's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB shard group's VPC. Access to the DB shard group is ultimately controlled by the security group it uses. That public access is not permitted if the security group assigned to the DB shard group doesn't permit it.</p> <p>When the DB shard group isn't publicly accessible, it is an internal DB shard group with a DNS name that resolves to a private IP address.</p> <p>Default: The default behavior varies depending on whether <code>DBSubnetGroupName</code> is specified.</p> <p>If <code>DBSubnetGroupName</code> isn't specified, and <code>PubliclyAccessible</code> isn't specified, the following applies:</p> <ul> <li> <p>If the default VPC in the target Region doesn’t have an internet gateway attached to it, the DB shard group is private.</p> </li> <li> <p>If the default VPC in the target Region has an internet gateway attached to it, the DB shard group is public.</p> </li> </ul> <p>If <code>DBSubnetGroupName</code> is specified, and <code>PubliclyAccessible</code> isn't specified, the following applies:</p> <ul> <li> <p>If the subnets are part of a VPC that doesn’t have an internet gateway attached to it, the DB shard group is private.</p> </li> <li> <p>If the subnets are part of a VPC that has an internet gateway attached to it, the DB shard group is public.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBShardGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_shard_group_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBShardGroupIdentifier",
                str(value["db_shard_group_identifier"]),
            )
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "compute_redundancy" in value:
        pairs.append((f"{prefix}.ComputeRedundancy", str(value["compute_redundancy"])))
    if "max_acu" in value:
        pairs.append((f"{prefix}.MaxACU", str(value["max_acu"])))
    if "min_acu" in value:
        pairs.append((f"{prefix}.MinACU", str(value["min_acu"])))
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{prefix}.PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "tags" in value:
        import aws_sdk_rds.types.tag_list

        aws_sdk_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateDBShardGroupMessage:
    out: CreateDBShardGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_shard_group_identifier = el.find("DBShardGroupIdentifier")
    if child_db_shard_group_identifier is not None:
        out["db_shard_group_identifier"] = str(
            child_db_shard_group_identifier.text or ""
        )
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_compute_redundancy = el.find("ComputeRedundancy")
    if child_compute_redundancy is not None:
        out["compute_redundancy"] = int(child_compute_redundancy.text or "")
    child_max_acu = el.find("MaxACU")
    if child_max_acu is not None:
        out["max_acu"] = float(child_max_acu.text or "")
    child_min_acu = el.find("MinACU")
    if child_min_acu is not None:
        out["min_acu"] = float(child_min_acu.text or "")
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_rds.types.tag_list

        out["tags"] = aws_sdk_rds.types.tag_list.deserialize_query(child_tags)
    return out
