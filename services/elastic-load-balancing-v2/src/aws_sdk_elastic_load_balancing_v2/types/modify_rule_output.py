"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyRuleOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.rules


class ModifyRuleOutput(TypedDict):
    rules: NotRequired["aws_sdk_elastic_load_balancing_v2.types.rules.Rules"]
    """<p>Information about the modified rule.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyRuleOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rules" in value:
        import aws_sdk_elastic_load_balancing_v2.types.rules

        aws_sdk_elastic_load_balancing_v2.types.rules.serialize_query(
            value["rules"], pairs, f"{prefix}.Rules"
        )


def deserialize_query(el: Element) -> ModifyRuleOutput:
    out: ModifyRuleOutput = {}  # type: ignore[typeddict-item]
    child_rules = el.find("Rules")
    if child_rules is not None:
        import aws_sdk_elastic_load_balancing_v2.types.rules

        out["rules"] = aws_sdk_elastic_load_balancing_v2.types.rules.deserialize_query(
            child_rules
        )
    return out
