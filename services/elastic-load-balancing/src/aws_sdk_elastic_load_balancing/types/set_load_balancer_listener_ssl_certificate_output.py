"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#SetLoadBalancerListenerSSLCertificateOutput``."""

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element


class SetLoadBalancerListenerSSLCertificateOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetLoadBalancerListenerSSLCertificateOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> SetLoadBalancerListenerSSLCertificateOutput:
    out: SetLoadBalancerListenerSSLCertificateOutput = {}  # type: ignore[typeddict-item]
    return out
