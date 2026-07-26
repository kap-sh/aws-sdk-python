"""Generated from Smithy shape ``com.amazonaws.docdb#DescribeEventCategoriesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.filter_list
    import capo_docdb.types.string


class DescribeEventCategoriesMessage(TypedDict, closed=True):
    source_type: NotRequired["capo_docdb.types.string.String"]
    """<p>The type of source that is generating the events.</p> <p>Valid values: <code>db-instance</code>, <code>db-parameter-group</code>, <code>db-security-group</code> </p>"""
    filters: NotRequired["capo_docdb.types.filter_list.FilterList"]
    """<p>This parameter is not currently supported.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEventCategoriesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_type" in value:
        pairs.append((f"{prefix}.SourceType", str(value["source_type"])))
    if "filters" in value:
        import capo_docdb.types.filter_list

        capo_docdb.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )


def deserialize_query(el: Element) -> DescribeEventCategoriesMessage:
    out: DescribeEventCategoriesMessage = {}  # type: ignore[typeddict-item]
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        out["source_type"] = str(child_source_type.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_docdb.types.filter_list

        out["filters"] = capo_docdb.types.filter_list.deserialize_query(child_filters)
    return out
