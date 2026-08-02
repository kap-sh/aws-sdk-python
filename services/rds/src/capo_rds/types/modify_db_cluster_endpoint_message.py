"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBClusterEndpointMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.string_list


class ModifyDBClusterEndpointMessage(TypedDict, closed=True):
    db_cluster_endpoint_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the endpoint to modify. This parameter is stored as a lowercase string.</p>"""
    endpoint_type: NotRequired["capo_rds.types.string.String"]
    """<p>The type of the endpoint. One of: <code>READER</code>, <code>WRITER</code>, <code>ANY</code>.</p>"""
    static_members: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>List of DB instance identifiers that are part of the custom endpoint group.</p>"""
    excluded_members: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBClusterEndpointMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_endpoint_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterEndpointIdentifier",
                str(value["db_cluster_endpoint_identifier"]),
            )
        )
    if "endpoint_type" in value:
        pairs.append((f"{key_prefix}EndpointType", str(value["endpoint_type"])))
    if "static_members" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["static_members"], pairs, f"{key_prefix}StaticMembers"
        )
    if "excluded_members" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["excluded_members"], pairs, f"{key_prefix}ExcludedMembers"
        )


def deserialize_query(el: Element) -> ModifyDBClusterEndpointMessage:
    out: ModifyDBClusterEndpointMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_endpoint_identifier = el.find("DBClusterEndpointIdentifier")
    if child_db_cluster_endpoint_identifier is not None:
        out["db_cluster_endpoint_identifier"] = str(
            child_db_cluster_endpoint_identifier.text or ""
        )
    child_endpoint_type = el.find("EndpointType")
    if child_endpoint_type is not None:
        out["endpoint_type"] = str(child_endpoint_type.text or "")
    child_static_members = el.find("StaticMembers")
    if child_static_members is not None:
        import capo_rds.types.string_list

        out["static_members"] = capo_rds.types.string_list.deserialize_query(
            child_static_members
        )
    child_excluded_members = el.find("ExcludedMembers")
    if child_excluded_members is not None:
        import capo_rds.types.string_list

        out["excluded_members"] = capo_rds.types.string_list.deserialize_query(
            child_excluded_members
        )
    return out
