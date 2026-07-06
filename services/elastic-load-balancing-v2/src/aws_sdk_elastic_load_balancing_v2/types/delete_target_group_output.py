"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DeleteTargetGroupOutput``."""

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element


class DeleteTargetGroupOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteTargetGroupOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteTargetGroupOutput:
    out: DeleteTargetGroupOutput = {}  # type: ignore[typeddict-item]
    return out
