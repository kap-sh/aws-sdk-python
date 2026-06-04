"""Generated from Smithy shape ``com.amazonaws.iam#ListOpenIDConnectProvidersRequest``."""

from typing import TypedDict
from aws_sdk_iam._protocol.xml import Element


class ListOpenIDConnectProvidersRequest(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: ListOpenIDConnectProvidersRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> ListOpenIDConnectProvidersRequest:
    out: ListOpenIDConnectProvidersRequest = {}  # type: ignore[typeddict-item]
    return out
