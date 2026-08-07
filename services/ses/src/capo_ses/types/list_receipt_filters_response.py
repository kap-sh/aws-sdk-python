"""Generated from Smithy shape ``com.amazonaws.ses#ListReceiptFiltersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.receipt_filter_list


class ListReceiptFiltersResponse(TypedDict, closed=True):
    filters: NotRequired["capo_ses.types.receipt_filter_list.ReceiptFilterList"]
    """<p>A list of IP address filter data structures, which each consist of a name, an IP address range, and whether to allow or block mail from it.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListReceiptFiltersResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "filters" in value:
        import capo_ses.types.receipt_filter_list

        capo_ses.types.receipt_filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )


def deserialize_query(el: Element) -> ListReceiptFiltersResponse:
    out: ListReceiptFiltersResponse = {}  # type: ignore[typeddict-item]
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_ses.types.receipt_filter_list

        out["filters"] = capo_ses.types.receipt_filter_list.deserialize_query(
            child_filters
        )
    return out
