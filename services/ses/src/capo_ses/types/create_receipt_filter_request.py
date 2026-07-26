"""Generated from Smithy shape ``com.amazonaws.ses#CreateReceiptFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.receipt_filter


class CreateReceiptFilterRequest(TypedDict, closed=True):
    filter: "capo_ses.types.receipt_filter.ReceiptFilter"
    """<p>A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateReceiptFilterRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.receipt_filter

    capo_ses.types.receipt_filter.serialize_query(
        value["filter"], pairs, f"{prefix}.Filter"
    )


def deserialize_query(el: Element) -> CreateReceiptFilterRequest:
    out: CreateReceiptFilterRequest = {}  # type: ignore[typeddict-item]
    child_filter = el.find("Filter")
    if child_filter is not None:
        import capo_ses.types.receipt_filter

        out["filter"] = capo_ses.types.receipt_filter.deserialize_query(child_filter)
    else:
        raise DeserializationError("CreateReceiptFilterRequest.filter required")
    return out
