"""Generated from Smithy shape ``com.amazonaws.sns#UntagResourceResponse``."""

from typing import TypedDict

from aws_sdk_sns._protocol.xml import Element


class UntagResourceResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagResourceResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> UntagResourceResponse:
    out: UntagResourceResponse = {}  # type: ignore[typeddict-item]
    return out
