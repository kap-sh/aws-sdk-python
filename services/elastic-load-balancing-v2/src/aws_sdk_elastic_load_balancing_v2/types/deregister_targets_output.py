"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DeregisterTargetsOutput``."""

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element


class DeregisterTargetsOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeregisterTargetsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeregisterTargetsOutput:
    out: DeregisterTargetsOutput = {}  # type: ignore[typeddict-item]
    return out
