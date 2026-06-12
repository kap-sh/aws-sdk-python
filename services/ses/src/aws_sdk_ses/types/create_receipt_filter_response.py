"""Generated from Smithy shape ``com.amazonaws.ses#CreateReceiptFilterResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class CreateReceiptFilterResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateReceiptFilterResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> CreateReceiptFilterResponse:
    out: CreateReceiptFilterResponse = {}  # type: ignore[typeddict-item]
    return out
