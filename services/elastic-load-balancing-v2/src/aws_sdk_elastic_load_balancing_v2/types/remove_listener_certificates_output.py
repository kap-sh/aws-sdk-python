"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RemoveListenerCertificatesOutput``."""

from typing import TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element


class RemoveListenerCertificatesOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveListenerCertificatesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> RemoveListenerCertificatesOutput:
    out: RemoveListenerCertificatesOutput = {}  # type: ignore[typeddict-item]
    return out
