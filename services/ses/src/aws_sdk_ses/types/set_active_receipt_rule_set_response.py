"""Generated from Smithy shape ``com.amazonaws.ses#SetActiveReceiptRuleSetResponse``."""

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element


class SetActiveReceiptRuleSetResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetActiveReceiptRuleSetResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> SetActiveReceiptRuleSetResponse:
    out: SetActiveReceiptRuleSetResponse = {}  # type: ignore[typeddict-item]
    return out
