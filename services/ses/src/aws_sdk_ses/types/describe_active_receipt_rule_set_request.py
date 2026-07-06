"""Generated from Smithy shape ``com.amazonaws.ses#DescribeActiveReceiptRuleSetRequest``."""

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element


class DescribeActiveReceiptRuleSetRequest(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeActiveReceiptRuleSetRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> DescribeActiveReceiptRuleSetRequest:
    out: DescribeActiveReceiptRuleSetRequest = {}  # type: ignore[typeddict-item]
    return out
