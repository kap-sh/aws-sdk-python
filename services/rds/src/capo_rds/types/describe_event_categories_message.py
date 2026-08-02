"""Generated from Smithy shape ``com.amazonaws.rds#DescribeEventCategoriesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.filter_list
    import capo_rds.types.string


class DescribeEventCategoriesMessage(TypedDict, closed=True):
    source_type: NotRequired["capo_rds.types.string.String"]
    """<p>The type of source that is generating the events. For RDS Proxy events, specify <code>db-proxy</code>.</p> <p>Valid Values: <code>db-instance</code> | <code>db-cluster</code> | <code>db-parameter-group</code> | <code>db-security-group</code> | <code>db-snapshot</code> | <code>db-cluster-snapshot</code> | <code>db-proxy</code> </p>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>This parameter isn't currently supported.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEventCategoriesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_type" in value:
        pairs.append((f"{key_prefix}SourceType", str(value["source_type"])))
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )


def deserialize_query(el: Element) -> DescribeEventCategoriesMessage:
    out: DescribeEventCategoriesMessage = {}  # type: ignore[typeddict-item]
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        out["source_type"] = str(child_source_type.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_rds.types.filter_list

        out["filters"] = capo_rds.types.filter_list.deserialize_query(child_filters)
    return out
