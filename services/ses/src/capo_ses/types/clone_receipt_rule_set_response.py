"""Generated from Smithy shape ``com.amazonaws.ses#CloneReceiptRuleSetResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class CloneReceiptRuleSetResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CloneReceiptRuleSetResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> CloneReceiptRuleSetResponse:
    out: CloneReceiptRuleSetResponse = {}  # type: ignore[typeddict-item]
    return out
