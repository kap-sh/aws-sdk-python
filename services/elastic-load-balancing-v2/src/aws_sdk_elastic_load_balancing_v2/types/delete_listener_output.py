"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DeleteListenerOutput``."""

from typing import TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element


class DeleteListenerOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteListenerOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteListenerOutput:
    out: DeleteListenerOutput = {}  # type: ignore[typeddict-item]
    return out
