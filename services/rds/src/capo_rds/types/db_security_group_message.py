"""Generated from Smithy shape ``com.amazonaws.rds#DBSecurityGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_security_groups
    import capo_rds.types.string


class DBSecurityGroupMessage(TypedDict, closed=True):
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_security_groups: NotRequired[
        "capo_rds.types.db_security_groups.DBSecurityGroups"
    ]
    """<p>A list of <code>DBSecurityGroup</code> instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSecurityGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_security_groups" in value:
        import capo_rds.types.db_security_groups

        capo_rds.types.db_security_groups.serialize_query(
            value["db_security_groups"], pairs, f"{prefix}.DBSecurityGroups"
        )


def deserialize_query(el: Element) -> DBSecurityGroupMessage:
    out: DBSecurityGroupMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_security_groups = el.find("DBSecurityGroups")
    if child_db_security_groups is not None:
        import capo_rds.types.db_security_groups

        out["db_security_groups"] = capo_rds.types.db_security_groups.deserialize_query(
            child_db_security_groups
        )
    return out
