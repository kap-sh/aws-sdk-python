"""Generated from Smithy shape ``com.amazonaws.ses#DeleteReceiptRuleResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class DeleteReceiptRuleResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteReceiptRuleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteReceiptRuleResponse:
    out: DeleteReceiptRuleResponse = {}  # type: ignore[typeddict-item]
    return out
