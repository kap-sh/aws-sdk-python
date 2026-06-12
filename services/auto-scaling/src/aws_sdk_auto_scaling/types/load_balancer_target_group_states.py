"""Generated from Smithy shape ``com.amazonaws.autoscaling#LoadBalancerTargetGroupStates``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.load_balancer_target_group_state

LoadBalancerTargetGroupStates: TypeAlias = list[
    "aws_sdk_auto_scaling.types.load_balancer_target_group_state.LoadBalancerTargetGroupState"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerTargetGroupStates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.load_balancer_target_group_state

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.load_balancer_target_group_state.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LoadBalancerTargetGroupStates:
    import aws_sdk_auto_scaling.types.load_balancer_target_group_state

    out: LoadBalancerTargetGroupStates = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_auto_scaling.types.load_balancer_target_group_state.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: LoadBalancerTargetGroupStates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.load_balancer_target_group_state

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.load_balancer_target_group_state.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LoadBalancerTargetGroupStates:
    import aws_sdk_auto_scaling.types.load_balancer_target_group_state

    out: LoadBalancerTargetGroupStates = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_auto_scaling.types.load_balancer_target_group_state.deserialize_query(
                child
            )
        )
    return out
