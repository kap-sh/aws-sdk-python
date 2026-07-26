"""Generated from Smithy shape ``com.amazonaws.ses#SetReceiptRulePositionResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class SetReceiptRulePositionResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetReceiptRulePositionResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> SetReceiptRulePositionResponse:
    out: SetReceiptRulePositionResponse = {}  # type: ignore[typeddict-item]
    return out
