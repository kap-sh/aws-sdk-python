"""Generated from Smithy shape ``com.amazonaws.rds#DeregisterDBProxyTargetsResponse``."""

from typing import TypedDict

from aws_sdk_rds._protocol.xml import Element


class DeregisterDBProxyTargetsResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeregisterDBProxyTargetsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeregisterDBProxyTargetsResponse:
    out: DeregisterDBProxyTargetsResponse = {}  # type: ignore[typeddict-item]
    return out
