"""Generated from Smithy shape ``com.amazonaws.ses#CloneReceiptRuleSetResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class CloneReceiptRuleSetResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CloneReceiptRuleSetResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> CloneReceiptRuleSetResponse:
    out: CloneReceiptRuleSetResponse = {}  # type: ignore[typeddict-item]
    return out
