"""Generated from Smithy shape ``com.amazonaws.ses#DeleteReceiptRuleSetResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class DeleteReceiptRuleSetResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteReceiptRuleSetResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteReceiptRuleSetResponse:
    out: DeleteReceiptRuleSetResponse = {}  # type: ignore[typeddict-item]
    return out
