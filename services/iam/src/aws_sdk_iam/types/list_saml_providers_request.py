"""Generated from Smithy shape ``com.amazonaws.iam#ListSAMLProvidersRequest``."""

from typing import TypedDict
from aws_sdk_iam._protocol.xml import Element


class ListSAMLProvidersRequest(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: ListSAMLProvidersRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> ListSAMLProvidersRequest:
    out: ListSAMLProvidersRequest = {}  # type: ignore[typeddict-item]
    return out
