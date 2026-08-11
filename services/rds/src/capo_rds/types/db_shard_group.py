"""Generated from Smithy shape ``com.amazonaws.rds#DBShardGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.db_shard_group_identifier
    import capo_rds.types.double_optional
    import capo_rds.types.integer_optional
    import capo_rds.types.string
    import capo_rds.types.tag_list


class DBShardGroup(TypedDict, closed=True):
    db_shard_group_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services Region-unique, immutable identifier for the DB shard group.</p>"""
    db_shard_group_identifier: NotRequired[
        "capo_rds.types.db_shard_group_identifier.DBShardGroupIdentifier"
    ]
    """<p>The name of the DB shard group.</p>"""
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the primary DB cluster for the DB shard group.</p>"""
    max_acu: NotRequired["capo_rds.types.double_optional.DoubleOptional"]
    """<p>The maximum capacity of the DB shard group in Aurora capacity units (ACUs).</p>"""
    min_acu: NotRequired["capo_rds.types.double_optional.DoubleOptional"]
    """<p>The minimum capacity of the DB shard group in Aurora capacity units (ACUs).</p>"""
    compute_redundancy: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>Specifies whether to create standby DB shard groups for the DB shard group. Valid values are the following:</p> <ul> <li> <p>0 - Creates a DB shard group without a standby DB shard group. This is the default value.</p> </li> <li> <p>1 - Creates a DB shard group with a standby DB shard group in a different Availability Zone (AZ).</p> </li> <li> <p>2 - Creates a DB shard group with two standby DB shard groups in two different AZs.</p> </li> </ul>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the DB shard group.</p>"""
    publicly_accessible: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the DB shard group is publicly accessible.</p> <p>When the DB shard group is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB shard group's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB shard group's VPC. Access to the DB shard group is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB shard group doesn't permit it.</p> <p>When the DB shard group isn't publicly accessible, it is an internal DB shard group with a DNS name that resolves to a private IP address.</p> <p>For more information, see <a>CreateDBShardGroup</a>.</p> <p>This setting is only for Aurora Limitless Database.</p>"""
    endpoint: NotRequired["capo_rds.types.string.String"]
    """<p>The connection endpoint for the DB shard group.</p>"""
    db_shard_group_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB shard group.</p>"""
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBShardGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_shard_group_resource_id" in value:
        pairs.append(
            (
                f"{key_prefix}DBShardGroupResourceId",
                str(value["db_shard_group_resource_id"]),
            )
        )
    if "db_shard_group_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBShardGroupIdentifier",
                str(value["db_shard_group_identifier"]),
            )
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "max_acu" in value:
        pairs.append(
            (
                f"{key_prefix}MaxACU",
                (
                    "NaN"
                    if value["max_acu"] != value["max_acu"]
                    else "Infinity"
                    if value["max_acu"] == float("inf")
                    else "-Infinity"
                    if value["max_acu"] == float("-inf")
                    else str(value["max_acu"])
                ),
            )
        )
    if "min_acu" in value:
        pairs.append(
            (
                f"{key_prefix}MinACU",
                (
                    "NaN"
                    if value["min_acu"] != value["min_acu"]
                    else "Infinity"
                    if value["min_acu"] == float("inf")
                    else "-Infinity"
                    if value["min_acu"] == float("-inf")
                    else str(value["min_acu"])
                ),
            )
        )
    if "compute_redundancy" in value:
        pairs.append(
            (f"{key_prefix}ComputeRedundancy", str(value["compute_redundancy"]))
        )
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "endpoint" in value:
        pairs.append((f"{key_prefix}Endpoint", str(value["endpoint"])))
    if "db_shard_group_arn" in value:
        pairs.append((f"{key_prefix}DBShardGroupArn", str(value["db_shard_group_arn"])))
    if "tag_list" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{key_prefix}TagList"
        )


def deserialize_query(el: Element) -> DBShardGroup:
    out: DBShardGroup = {}  # type: ignore[typeddict-item]
    child_db_shard_group_resource_id = el.find("DBShardGroupResourceId")
    if child_db_shard_group_resource_id is not None:
        out["db_shard_group_resource_id"] = str(
            child_db_shard_group_resource_id.text or ""
        )
    child_db_shard_group_identifier = el.find("DBShardGroupIdentifier")
    if child_db_shard_group_identifier is not None:
        out["db_shard_group_identifier"] = str(
            child_db_shard_group_identifier.text or ""
        )
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_max_acu = el.find("MaxACU")
    if child_max_acu is not None:
        out["max_acu"] = float(child_max_acu.text or "")
    child_min_acu = el.find("MinACU")
    if child_min_acu is not None:
        out["min_acu"] = float(child_min_acu.text or "")
    child_compute_redundancy = el.find("ComputeRedundancy")
    if child_compute_redundancy is not None:
        out["compute_redundancy"] = int(child_compute_redundancy.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    child_db_shard_group_arn = el.find("DBShardGroupArn")
    if child_db_shard_group_arn is not None:
        out["db_shard_group_arn"] = str(child_db_shard_group_arn.text or "")
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    return out
