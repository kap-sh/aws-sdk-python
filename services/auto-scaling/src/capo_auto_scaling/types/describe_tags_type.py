"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeTagsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.filters
    import capo_auto_scaling.types.max_records
    import capo_auto_scaling.types.xml_string


class DescribeTagsType(TypedDict, closed=True):
    filters: NotRequired["capo_auto_scaling.types.filters.Filters"]
    """<p>One or more filters to scope the tags to return. The maximum number of filters per filter type (for example, <code>auto-scaling-group</code>) is 1000.</p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_records: NotRequired["capo_auto_scaling.types.max_records.MaxRecords"]
    """<p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTagsType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "filters" in value:
        import capo_auto_scaling.types.filters

        capo_auto_scaling.types.filters.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeTagsType:
    out: DescribeTagsType = {}  # type: ignore[typeddict-item]
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_auto_scaling.types.filters

        out["filters"] = capo_auto_scaling.types.filters.deserialize_query(
            child_filters
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
