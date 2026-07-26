"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.rules


class CreateRuleOutput(TypedDict, closed=True):
    rules: NotRequired["capo_elastic_load_balancing_v2.types.rules.Rules"]
    """<p>Information about the rule.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateRuleOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rules" in value:
        import capo_elastic_load_balancing_v2.types.rules

        capo_elastic_load_balancing_v2.types.rules.serialize_query(
            value["rules"], pairs, f"{prefix}.Rules"
        )


def deserialize_query(el: Element) -> CreateRuleOutput:
    out: CreateRuleOutput = {}  # type: ignore[typeddict-item]
    child_rules = el.find("Rules")
    if child_rules is not None:
        import capo_elastic_load_balancing_v2.types.rules

        out["rules"] = capo_elastic_load_balancing_v2.types.rules.deserialize_query(
            child_rules
        )
    return out
