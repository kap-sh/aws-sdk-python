"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RegisterTargetsOutput``."""

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element


class RegisterTargetsOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: RegisterTargetsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> RegisterTargetsOutput:
    out: RegisterTargetsOutput = {}  # type: ignore[typeddict-item]
    return out
