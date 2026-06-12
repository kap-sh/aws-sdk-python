"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RemoveTrustStoreRevocationsOutput``."""

from typing import TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element


class RemoveTrustStoreRevocationsOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveTrustStoreRevocationsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> RemoveTrustStoreRevocationsOutput:
    out: RemoveTrustStoreRevocationsOutput = {}  # type: ignore[typeddict-item]
    return out
