"""Generated from Smithy shape ``com.amazonaws.sns#TagResourceResponse``."""

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element


class TagResourceResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: TagResourceResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> TagResourceResponse:
    out: TagResourceResponse = {}  # type: ignore[typeddict-item]
    return out
