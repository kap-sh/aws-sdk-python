"""Generated from Smithy shape ``com.amazonaws.sts#GetCallerIdentityRequest``."""

from typing import TypedDict

from aws_sdk_sts._protocol.xml import Element


class GetCallerIdentityRequest(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: GetCallerIdentityRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> GetCallerIdentityRequest:
    out: GetCallerIdentityRequest = {}  # type: ignore[typeddict-item]
    return out
