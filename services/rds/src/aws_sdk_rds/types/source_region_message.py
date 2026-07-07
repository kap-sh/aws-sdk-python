"""Generated from Smithy shape ``com.amazonaws.rds#SourceRegionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.source_region_list
    import aws_sdk_rds.types.string


class SourceRegionMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    source_regions: NotRequired["aws_sdk_rds.types.source_region_list.SourceRegionList"]
    """<p>A list of <code>SourceRegion</code> instances that contains each source Amazon Web Services Region that the current Amazon Web Services Region can get a read replica or a DB snapshot from.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SourceRegionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "source_regions" in value:
        import aws_sdk_rds.types.source_region_list

        aws_sdk_rds.types.source_region_list.serialize_query(
            value["source_regions"], pairs, f"{prefix}.SourceRegions"
        )


def deserialize_query(el: Element) -> SourceRegionMessage:
    out: SourceRegionMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_source_regions = el.find("SourceRegions")
    if child_source_regions is not None:
        import aws_sdk_rds.types.source_region_list

        out["source_regions"] = aws_sdk_rds.types.source_region_list.deserialize_query(
            child_source_regions
        )
    return out
