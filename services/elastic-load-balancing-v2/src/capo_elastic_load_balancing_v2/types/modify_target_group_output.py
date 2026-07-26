"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyTargetGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.target_groups


class ModifyTargetGroupOutput(TypedDict, closed=True):
    target_groups: NotRequired[
        "capo_elastic_load_balancing_v2.types.target_groups.TargetGroups"
    ]
    """<p>Information about the modified target group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyTargetGroupOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_groups" in value:
        import capo_elastic_load_balancing_v2.types.target_groups

        capo_elastic_load_balancing_v2.types.target_groups.serialize_query(
            value["target_groups"], pairs, f"{prefix}.TargetGroups"
        )


def deserialize_query(el: Element) -> ModifyTargetGroupOutput:
    out: ModifyTargetGroupOutput = {}  # type: ignore[typeddict-item]
    child_target_groups = el.find("TargetGroups")
    if child_target_groups is not None:
        import capo_elastic_load_balancing_v2.types.target_groups

        out["target_groups"] = (
            capo_elastic_load_balancing_v2.types.target_groups.deserialize_query(
                child_target_groups
            )
        )
    return out
