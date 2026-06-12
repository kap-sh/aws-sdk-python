"""Generated from Smithy shape ``com.amazonaws.docdb#DBInstanceMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.db_instance_list
    import aws_sdk_docdb.types.string


class DBInstanceMessage(TypedDict):
    marker: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_instances: NotRequired["aws_sdk_docdb.types.db_instance_list.DBInstanceList"]
    """<p>Detailed information about one or more instances. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_instances" in value:
        import aws_sdk_docdb.types.db_instance_list

        aws_sdk_docdb.types.db_instance_list.serialize_query(
            value["db_instances"], pairs, f"{prefix}.DBInstances"
        )


def deserialize_query(el: Element) -> DBInstanceMessage:
    out: DBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_instances = el.find("DBInstances")
    if child_db_instances is not None:
        import aws_sdk_docdb.types.db_instance_list

        out["db_instances"] = aws_sdk_docdb.types.db_instance_list.deserialize_query(
            child_db_instances
        )
    return out
