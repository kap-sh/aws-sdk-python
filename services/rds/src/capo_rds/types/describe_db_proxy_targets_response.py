"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBProxyTargetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.target_list


class DescribeDBProxyTargetsResponse(TypedDict, closed=True):
    targets: NotRequired["capo_rds.types.target_list.TargetList"]
    """<p>An arbitrary number of <code>DBProxyTarget</code> objects, containing details of the corresponding targets.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBProxyTargetsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "targets" in value:
        import capo_rds.types.target_list

        capo_rds.types.target_list.serialize_query(
            value["targets"], pairs, f"{key_prefix}Targets"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBProxyTargetsResponse:
    out: DescribeDBProxyTargetsResponse = {}  # type: ignore[typeddict-item]
    child_targets = el.find("Targets")
    if child_targets is not None:
        import capo_rds.types.target_list

        out["targets"] = capo_rds.types.target_list.deserialize_query(child_targets)
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
