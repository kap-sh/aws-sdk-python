"""Generated from Smithy shape ``com.amazonaws.ses#CreateReceiptRuleSetResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class CreateReceiptRuleSetResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateReceiptRuleSetResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> CreateReceiptRuleSetResponse:
    out: CreateReceiptRuleSetResponse = {}  # type: ignore[typeddict-item]
    return out
