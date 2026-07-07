"""Generated from Smithy shape ``com.amazonaws.docdb#DBSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.db_subnet_groups
    import aws_sdk_docdb.types.string


class DBSubnetGroupMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_subnet_groups: NotRequired["aws_sdk_docdb.types.db_subnet_groups.DBSubnetGroups"]
    """<p>Detailed information about one or more subnet groups.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_subnet_groups" in value:
        import aws_sdk_docdb.types.db_subnet_groups

        aws_sdk_docdb.types.db_subnet_groups.serialize_query(
            value["db_subnet_groups"], pairs, f"{prefix}.DBSubnetGroups"
        )


def deserialize_query(el: Element) -> DBSubnetGroupMessage:
    out: DBSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_subnet_groups = el.find("DBSubnetGroups")
    if child_db_subnet_groups is not None:
        import aws_sdk_docdb.types.db_subnet_groups

        out["db_subnet_groups"] = (
            aws_sdk_docdb.types.db_subnet_groups.deserialize_query(
                child_db_subnet_groups
            )
        )
    return out
