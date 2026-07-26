"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DeleteRuleOutput``."""

from typing_extensions import TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element


class DeleteRuleOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteRuleOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteRuleOutput:
    out: DeleteRuleOutput = {}  # type: ignore[typeddict-item]
    return out
