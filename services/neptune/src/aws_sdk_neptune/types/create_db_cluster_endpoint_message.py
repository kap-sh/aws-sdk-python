"""Generated from Smithy shape ``com.amazonaws.neptune#CreateDBClusterEndpointMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string
    import aws_sdk_neptune.types.string_list
    import aws_sdk_neptune.types.tag_list


class CreateDBClusterEndpointMessage(TypedDict):
    db_cluster_identifier: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.</p>"""
    db_cluster_endpoint_identifier: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The identifier to use for the new endpoint. This parameter is stored as a lowercase string.</p>"""
    endpoint_type: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The type of the endpoint. One of: <code>READER</code>, <code>WRITER</code>, <code>ANY</code>.</p>"""
    static_members: NotRequired["aws_sdk_neptune.types.string_list.StringList"]
    """<p>List of DB instance identifiers that are part of the custom endpoint group.</p>"""
    excluded_members: NotRequired["aws_sdk_neptune.types.string_list.StringList"]
    """<p>List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.</p>"""
    tags: NotRequired["aws_sdk_neptune.types.tag_list.TagList"]
    """<p>The tags to be assigned to the Amazon Neptune resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBClusterEndpointMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "db_cluster_endpoint_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterEndpointIdentifier",
                str(value["db_cluster_endpoint_identifier"]),
            )
        )
    if "endpoint_type" in value:
        pairs.append((f"{prefix}.EndpointType", str(value["endpoint_type"])))
    if "static_members" in value:
        import aws_sdk_neptune.types.string_list

        aws_sdk_neptune.types.string_list.serialize_query(
            value["static_members"], pairs, f"{prefix}.StaticMembers"
        )
    if "excluded_members" in value:
        import aws_sdk_neptune.types.string_list

        aws_sdk_neptune.types.string_list.serialize_query(
            value["excluded_members"], pairs, f"{prefix}.ExcludedMembers"
        )
    if "tags" in value:
        import aws_sdk_neptune.types.tag_list

        aws_sdk_neptune.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateDBClusterEndpointMessage:
    out: CreateDBClusterEndpointMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
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
        import aws_sdk_neptune.types.string_list

        out["static_members"] = aws_sdk_neptune.types.string_list.deserialize_query(
            child_static_members
        )
    child_excluded_members = el.find("ExcludedMembers")
    if child_excluded_members is not None:
        import aws_sdk_neptune.types.string_list

        out["excluded_members"] = aws_sdk_neptune.types.string_list.deserialize_query(
            child_excluded_members
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_neptune.types.tag_list

        out["tags"] = aws_sdk_neptune.types.tag_list.deserialize_query(child_tags)
    return out
