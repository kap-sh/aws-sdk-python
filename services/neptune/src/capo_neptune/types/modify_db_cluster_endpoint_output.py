"""Generated from Smithy shape ``com.amazonaws.neptune#ModifyDBClusterEndpointOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.string
    import capo_neptune.types.string_list


class ModifyDBClusterEndpointOutput(TypedDict, closed=True):
    db_cluster_endpoint_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The identifier associated with the endpoint. This parameter is stored as a lowercase string.</p>"""
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.</p>"""
    db_cluster_endpoint_resource_identifier: NotRequired[
        "capo_neptune.types.string.String"
    ]
    """<p>A unique system-generated identifier for an endpoint. It remains the same for the whole life of the endpoint.</p>"""
    endpoint: NotRequired["capo_neptune.types.string.String"]
    """<p>The DNS address of the endpoint.</p>"""
    status: NotRequired["capo_neptune.types.string.String"]
    """<p>The current status of the endpoint. One of: <code>creating</code>, <code>available</code>, <code>deleting</code>, <code>inactive</code>, <code>modifying</code>. The <code>inactive</code> state applies to an endpoint that cannot be used for a certain kind of cluster, such as a <code>writer</code> endpoint for a read-only secondary cluster in a global database.</p>"""
    endpoint_type: NotRequired["capo_neptune.types.string.String"]
    """<p>The type of the endpoint. One of: <code>READER</code>, <code>WRITER</code>, <code>CUSTOM</code>.</p>"""
    custom_endpoint_type: NotRequired["capo_neptune.types.string.String"]
    """<p>The type associated with a custom endpoint. One of: <code>READER</code>, <code>WRITER</code>, <code>ANY</code>.</p>"""
    static_members: NotRequired["capo_neptune.types.string_list.StringList"]
    """<p>List of DB instance identifiers that are part of the custom endpoint group.</p>"""
    excluded_members: NotRequired["capo_neptune.types.string_list.StringList"]
    """<p>List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.</p>"""
    db_cluster_endpoint_arn: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the endpoint.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBClusterEndpointOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_endpoint_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterEndpointIdentifier",
                str(value["db_cluster_endpoint_identifier"]),
            )
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "db_cluster_endpoint_resource_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterEndpointResourceIdentifier",
                str(value["db_cluster_endpoint_resource_identifier"]),
            )
        )
    if "endpoint" in value:
        pairs.append((f"{prefix}.Endpoint", str(value["endpoint"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "endpoint_type" in value:
        pairs.append((f"{prefix}.EndpointType", str(value["endpoint_type"])))
    if "custom_endpoint_type" in value:
        pairs.append(
            (f"{prefix}.CustomEndpointType", str(value["custom_endpoint_type"]))
        )
    if "static_members" in value:
        import capo_neptune.types.string_list

        capo_neptune.types.string_list.serialize_query(
            value["static_members"], pairs, f"{prefix}.StaticMembers"
        )
    if "excluded_members" in value:
        import capo_neptune.types.string_list

        capo_neptune.types.string_list.serialize_query(
            value["excluded_members"], pairs, f"{prefix}.ExcludedMembers"
        )
    if "db_cluster_endpoint_arn" in value:
        pairs.append(
            (f"{prefix}.DBClusterEndpointArn", str(value["db_cluster_endpoint_arn"]))
        )


def deserialize_query(el: Element) -> ModifyDBClusterEndpointOutput:
    out: ModifyDBClusterEndpointOutput = {}  # type: ignore[typeddict-item]
    child_db_cluster_endpoint_identifier = el.find("DBClusterEndpointIdentifier")
    if child_db_cluster_endpoint_identifier is not None:
        out["db_cluster_endpoint_identifier"] = str(
            child_db_cluster_endpoint_identifier.text or ""
        )
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_db_cluster_endpoint_resource_identifier = el.find(
        "DBClusterEndpointResourceIdentifier"
    )
    if child_db_cluster_endpoint_resource_identifier is not None:
        out["db_cluster_endpoint_resource_identifier"] = str(
            child_db_cluster_endpoint_resource_identifier.text or ""
        )
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_endpoint_type = el.find("EndpointType")
    if child_endpoint_type is not None:
        out["endpoint_type"] = str(child_endpoint_type.text or "")
    child_custom_endpoint_type = el.find("CustomEndpointType")
    if child_custom_endpoint_type is not None:
        out["custom_endpoint_type"] = str(child_custom_endpoint_type.text or "")
    child_static_members = el.find("StaticMembers")
    if child_static_members is not None:
        import capo_neptune.types.string_list

        out["static_members"] = capo_neptune.types.string_list.deserialize_query(
            child_static_members
        )
    child_excluded_members = el.find("ExcludedMembers")
    if child_excluded_members is not None:
        import capo_neptune.types.string_list

        out["excluded_members"] = capo_neptune.types.string_list.deserialize_query(
            child_excluded_members
        )
    child_db_cluster_endpoint_arn = el.find("DBClusterEndpointArn")
    if child_db_cluster_endpoint_arn is not None:
        out["db_cluster_endpoint_arn"] = str(child_db_cluster_endpoint_arn.text or "")
    return out
