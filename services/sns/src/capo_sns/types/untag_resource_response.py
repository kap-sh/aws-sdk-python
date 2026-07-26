"""Generated from Smithy shape ``com.amazonaws.sns#UntagResourceResponse``."""

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element


class UntagResourceResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagResourceResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> UntagResourceResponse:
    out: UntagResourceResponse = {}  # type: ignore[typeddict-item]
    return out
