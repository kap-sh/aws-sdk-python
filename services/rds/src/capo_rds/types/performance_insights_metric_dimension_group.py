"""Generated from Smithy shape ``com.amazonaws.rds#PerformanceInsightsMetricDimensionGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integer
    import capo_rds.types.string
    import capo_rds.types.string_list


class PerformanceInsightsMetricDimensionGroup(TypedDict, closed=True):
    dimensions: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>A list of specific dimensions from a dimension group. If this list isn't included, then all of the dimensions in the group were requested, or are present in the response.</p>"""
    group: NotRequired["capo_rds.types.string.String"]
    """<p>The available dimension groups for Performance Insights metric type.</p>"""
    limit: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The maximum number of items to fetch for this dimension group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PerformanceInsightsMetricDimensionGroup,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dimensions" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["dimensions"], pairs, f"{prefix}.Dimensions"
        )
    if "group" in value:
        pairs.append((f"{prefix}.Group", str(value["group"])))
    if "limit" in value:
        pairs.append((f"{prefix}.Limit", str(value["limit"])))


def deserialize_query(el: Element) -> PerformanceInsightsMetricDimensionGroup:
    out: PerformanceInsightsMetricDimensionGroup = {}  # type: ignore[typeddict-item]
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import capo_rds.types.string_list

        out["dimensions"] = capo_rds.types.string_list.deserialize_query(
            child_dimensions
        )
    child_group = el.find("Group")
    if child_group is not None:
        out["group"] = str(child_group.text or "")
    child_limit = el.find("Limit")
    if child_limit is not None:
        out["limit"] = int(child_limit.text or "")
    return out
