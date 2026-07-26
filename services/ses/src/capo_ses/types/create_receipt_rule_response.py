"""Generated from Smithy shape ``com.amazonaws.ses#CreateReceiptRuleResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class CreateReceiptRuleResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateReceiptRuleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> CreateReceiptRuleResponse:
    out: CreateReceiptRuleResponse = {}  # type: ignore[typeddict-item]
    return out
