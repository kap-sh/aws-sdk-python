"""Generated from Smithy shape ``com.amazonaws.neptune#DBSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.db_subnet_groups
    import capo_neptune.types.string


class DBSubnetGroupMessage(TypedDict, closed=True):
    marker: NotRequired["capo_neptune.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_subnet_groups: NotRequired["capo_neptune.types.db_subnet_groups.DBSubnetGroups"]
    """<p> A list of <a>DBSubnetGroup</a> instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_subnet_groups" in value:
        import capo_neptune.types.db_subnet_groups

        capo_neptune.types.db_subnet_groups.serialize_query(
            value["db_subnet_groups"], pairs, f"{prefix}.DBSubnetGroups"
        )


def deserialize_query(el: Element) -> DBSubnetGroupMessage:
    out: DBSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_subnet_groups = el.find("DBSubnetGroups")
    if child_db_subnet_groups is not None:
        import capo_neptune.types.db_subnet_groups

        out["db_subnet_groups"] = capo_neptune.types.db_subnet_groups.deserialize_query(
            child_db_subnet_groups
        )
    return out
