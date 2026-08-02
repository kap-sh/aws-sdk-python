"""Generated from Smithy shape ``com.amazonaws.rds#DBProxyTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integer
    import capo_rds.types.string
    import capo_rds.types.target_health
    import capo_rds.types.target_role
    import capo_rds.types.target_type


class DBProxyTarget(TypedDict, closed=True):
    target_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the RDS DB instance or Aurora DB cluster.</p>"""
    endpoint: NotRequired["capo_rds.types.string.String"]
    """<p>The writer endpoint for the RDS DB instance or Aurora DB cluster.</p>"""
    tracked_cluster_id: NotRequired["capo_rds.types.string.String"]
    """<p>The DB cluster identifier when the target represents an Aurora DB cluster. This field is blank when the target represents an RDS DB instance.</p>"""
    rds_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier representing the target. It can be the instance identifier for an RDS DB instance, or the cluster identifier for an Aurora DB cluster.</p>"""
    port: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The port that the RDS Proxy uses to connect to the target RDS DB instance or Aurora DB cluster.</p>"""
    type: NotRequired["capo_rds.types.target_type.TargetType"]
    """<p>Specifies the kind of database, such as an RDS DB instance or an Aurora DB cluster, that the target represents.</p>"""
    role: NotRequired["capo_rds.types.target_role.TargetRole"]
    """<p>A value that indicates whether the target of the proxy can be used for read/write or read-only operations.</p>"""
    target_health: NotRequired["capo_rds.types.target_health.TargetHealth"]
    """<p>Information about the connection health of the RDS Proxy target.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBProxyTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target_arn" in value:
        pairs.append((f"{key_prefix}TargetArn", str(value["target_arn"])))
    if "endpoint" in value:
        pairs.append((f"{key_prefix}Endpoint", str(value["endpoint"])))
    if "tracked_cluster_id" in value:
        pairs.append(
            (f"{key_prefix}TrackedClusterId", str(value["tracked_cluster_id"]))
        )
    if "rds_resource_id" in value:
        pairs.append((f"{key_prefix}RdsResourceId", str(value["rds_resource_id"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "type" in value:
        import capo_rds.types.target_type

        capo_rds.types.target_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "role" in value:
        import capo_rds.types.target_role

        capo_rds.types.target_role.serialize_query(
            value["role"], pairs, f"{key_prefix}Role"
        )
    if "target_health" in value:
        import capo_rds.types.target_health

        capo_rds.types.target_health.serialize_query(
            value["target_health"], pairs, f"{key_prefix}TargetHealth"
        )


def deserialize_query(el: Element) -> DBProxyTarget:
    out: DBProxyTarget = {}  # type: ignore[typeddict-item]
    child_target_arn = el.find("TargetArn")
    if child_target_arn is not None:
        out["target_arn"] = str(child_target_arn.text or "")
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    child_tracked_cluster_id = el.find("TrackedClusterId")
    if child_tracked_cluster_id is not None:
        out["tracked_cluster_id"] = str(child_tracked_cluster_id.text or "")
    child_rds_resource_id = el.find("RdsResourceId")
    if child_rds_resource_id is not None:
        out["rds_resource_id"] = str(child_rds_resource_id.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_rds.types.target_type

        out["type"] = capo_rds.types.target_type.deserialize_query(child_type)
    child_role = el.find("Role")
    if child_role is not None:
        import capo_rds.types.target_role

        out["role"] = capo_rds.types.target_role.deserialize_query(child_role)
    child_target_health = el.find("TargetHealth")
    if child_target_health is not None:
        import capo_rds.types.target_health

        out["target_health"] = capo_rds.types.target_health.deserialize_query(
            child_target_health
        )
    return out
