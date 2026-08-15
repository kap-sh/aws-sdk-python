"""Generated from Smithy shape ``com.amazonaws.iam#PutAccountPropertiesResponse``."""

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element


class PutAccountPropertiesResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: PutAccountPropertiesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> PutAccountPropertiesResponse:
    out: PutAccountPropertiesResponse = {}  # type: ignore[typeddict-item]
    return out
