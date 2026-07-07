"""Generated from Smithy shape ``com.amazonaws.rds#DeregisterDBProxyTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_proxy_name
    import aws_sdk_rds.types.db_proxy_target_group_name
    import aws_sdk_rds.types.string_list


class DeregisterDBProxyTargetsRequest(TypedDict, closed=True):
    db_proxy_name: NotRequired["aws_sdk_rds.types.db_proxy_name.DBProxyName"]
    """<p>The identifier of the <code>DBProxy</code> that is associated with the <code>DBProxyTargetGroup</code>.</p>"""
    target_group_name: NotRequired[
        "aws_sdk_rds.types.db_proxy_target_group_name.DBProxyTargetGroupName"
    ]
    """<p>The identifier of the <code>DBProxyTargetGroup</code>.</p>"""
    db_instance_identifiers: NotRequired["aws_sdk_rds.types.string_list.StringList"]
    """<p>One or more DB instance identifiers.</p>"""
    db_cluster_identifiers: NotRequired["aws_sdk_rds.types.string_list.StringList"]
    """<p>One or more DB cluster identifiers.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeregisterDBProxyTargetsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_name" in value:
        pairs.append((f"{prefix}.DBProxyName", str(value["db_proxy_name"])))
    if "target_group_name" in value:
        pairs.append((f"{prefix}.TargetGroupName", str(value["target_group_name"])))
    if "db_instance_identifiers" in value:
        import aws_sdk_rds.types.string_list

        aws_sdk_rds.types.string_list.serialize_query(
            value["db_instance_identifiers"], pairs, f"{prefix}.DBInstanceIdentifiers"
        )
    if "db_cluster_identifiers" in value:
        import aws_sdk_rds.types.string_list

        aws_sdk_rds.types.string_list.serialize_query(
            value["db_cluster_identifiers"], pairs, f"{prefix}.DBClusterIdentifiers"
        )


def deserialize_query(el: Element) -> DeregisterDBProxyTargetsRequest:
    out: DeregisterDBProxyTargetsRequest = {}  # type: ignore[typeddict-item]
    child_db_proxy_name = el.find("DBProxyName")
    if child_db_proxy_name is not None:
        out["db_proxy_name"] = str(child_db_proxy_name.text or "")
    child_target_group_name = el.find("TargetGroupName")
    if child_target_group_name is not None:
        out["target_group_name"] = str(child_target_group_name.text or "")
    child_db_instance_identifiers = el.find("DBInstanceIdentifiers")
    if child_db_instance_identifiers is not None:
        import aws_sdk_rds.types.string_list

        out["db_instance_identifiers"] = (
            aws_sdk_rds.types.string_list.deserialize_query(
                child_db_instance_identifiers
            )
        )
    child_db_cluster_identifiers = el.find("DBClusterIdentifiers")
    if child_db_cluster_identifiers is not None:
        import aws_sdk_rds.types.string_list

        out["db_cluster_identifiers"] = aws_sdk_rds.types.string_list.deserialize_query(
            child_db_cluster_identifiers
        )
    return out
