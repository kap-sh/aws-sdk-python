"""Generated from Smithy shape ``com.amazonaws.autoscaling#ScalingPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.scaling_policy

ScalingPolicies: TypeAlias = list[
    "capo_auto_scaling.types.scaling_policy.ScalingPolicy"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ScalingPolicies, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.scaling_policy

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.scaling_policy.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ScalingPolicies:
    import capo_auto_scaling.types.scaling_policy

    out: ScalingPolicies = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.scaling_policy.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ScalingPolicies, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.scaling_policy

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.scaling_policy.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ScalingPolicies:
    import capo_auto_scaling.types.scaling_policy

    out: ScalingPolicies = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.scaling_policy.deserialize_query(child))
    return out
