"""Generated from Smithy shape ``com.amazonaws.ses#ListReceiptFiltersRequest``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class ListReceiptFiltersRequest(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: ListReceiptFiltersRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> ListReceiptFiltersRequest:
    out: ListReceiptFiltersRequest = {}  # type: ignore[typeddict-item]
    return out
