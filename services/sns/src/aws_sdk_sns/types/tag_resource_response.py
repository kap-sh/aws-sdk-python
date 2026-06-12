"""Generated from Smithy shape ``com.amazonaws.sns#TagResourceResponse``."""

from typing import TypedDict

from aws_sdk_sns._protocol.xml import Element


class TagResourceResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: TagResourceResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> TagResourceResponse:
    out: TagResourceResponse = {}  # type: ignore[typeddict-item]
    return out
