"""Generated from Smithy shape ``com.amazonaws.iam#GetAccountPropertiesRequest``."""

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element


class GetAccountPropertiesRequest(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAccountPropertiesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> GetAccountPropertiesRequest:
    out: GetAccountPropertiesRequest = {}  # type: ignore[typeddict-item]
    return out
