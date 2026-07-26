"""Generated from Smithy shape ``com.amazonaws.ses#ReorderReceiptRuleSetResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class ReorderReceiptRuleSetResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: ReorderReceiptRuleSetResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> ReorderReceiptRuleSetResponse:
    out: ReorderReceiptRuleSetResponse = {}  # type: ignore[typeddict-item]
    return out
