"""Generated from Smithy shape ``com.amazonaws.ses#UpdateReceiptRuleResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class UpdateReceiptRuleResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateReceiptRuleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> UpdateReceiptRuleResponse:
    out: UpdateReceiptRuleResponse = {}  # type: ignore[typeddict-item]
    return out
