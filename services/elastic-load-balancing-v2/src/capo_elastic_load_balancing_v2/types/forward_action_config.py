"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ForwardActionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.target_group_list
    import capo_elastic_load_balancing_v2.types.target_group_stickiness_config


class ForwardActionConfig(TypedDict, closed=True):
    target_groups: NotRequired[
        "capo_elastic_load_balancing_v2.types.target_group_list.TargetGroupList"
    ]
    """<p>The target groups.</p>"""
    target_group_stickiness_config: NotRequired[
        "capo_elastic_load_balancing_v2.types.target_group_stickiness_config.TargetGroupStickinessConfig"
    ]
    """<p>The target group stickiness for the rule.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ForwardActionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target_groups" in value:
        import capo_elastic_load_balancing_v2.types.target_group_list

        capo_elastic_load_balancing_v2.types.target_group_list.serialize_query(
            value["target_groups"], pairs, f"{key_prefix}TargetGroups"
        )
    if "target_group_stickiness_config" in value:
        import capo_elastic_load_balancing_v2.types.target_group_stickiness_config

        capo_elastic_load_balancing_v2.types.target_group_stickiness_config.serialize_query(
            value["target_group_stickiness_config"],
            pairs,
            f"{key_prefix}TargetGroupStickinessConfig",
        )


def deserialize_query(el: Element) -> ForwardActionConfig:
    out: ForwardActionConfig = {}  # type: ignore[typeddict-item]
    child_target_groups = el.find("TargetGroups")
    if child_target_groups is not None:
        import capo_elastic_load_balancing_v2.types.target_group_list

        out["target_groups"] = (
            capo_elastic_load_balancing_v2.types.target_group_list.deserialize_query(
                child_target_groups
            )
        )
    child_target_group_stickiness_config = el.find("TargetGroupStickinessConfig")
    if child_target_group_stickiness_config is not None:
        import capo_elastic_load_balancing_v2.types.target_group_stickiness_config

        out["target_group_stickiness_config"] = (
            capo_elastic_load_balancing_v2.types.target_group_stickiness_config.deserialize_query(
                child_target_group_stickiness_config
            )
        )
    return out
