"""Generated from Smithy shape ``com.amazonaws.ec2#LoadBalancersConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.classic_load_balancers_config
    import aws_sdk_ec2.types.target_groups_config


class LoadBalancersConfig(TypedDict):
    classic_load_balancers_config: NotRequired[
        "aws_sdk_ec2.types.classic_load_balancers_config.ClassicLoadBalancersConfig"
    ]
    """<p>The Classic Load Balancers.</p>"""
    target_groups_config: NotRequired[
        "aws_sdk_ec2.types.target_groups_config.TargetGroupsConfig"
    ]
    """<p>The target groups.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LoadBalancersConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "classic_load_balancers_config" in value:
        import aws_sdk_ec2.types.classic_load_balancers_config

        aws_sdk_ec2.types.classic_load_balancers_config.serialize_ec2_query(
            value["classic_load_balancers_config"],
            pairs,
            f"{prefix}.ClassicLoadBalancersConfig",
        )
    if "target_groups_config" in value:
        import aws_sdk_ec2.types.target_groups_config

        aws_sdk_ec2.types.target_groups_config.serialize_ec2_query(
            value["target_groups_config"], pairs, f"{prefix}.TargetGroupsConfig"
        )


def deserialize_ec2_query(el: Element) -> LoadBalancersConfig:
    out: LoadBalancersConfig = {}  # type: ignore[typeddict-item]
    child_classic_load_balancers_config = el.find("ClassicLoadBalancersConfig")
    if child_classic_load_balancers_config is not None:
        import aws_sdk_ec2.types.classic_load_balancers_config

        out["classic_load_balancers_config"] = (
            aws_sdk_ec2.types.classic_load_balancers_config.deserialize_ec2_query(
                child_classic_load_balancers_config
            )
        )
    child_target_groups_config = el.find("TargetGroupsConfig")
    if child_target_groups_config is not None:
        import aws_sdk_ec2.types.target_groups_config

        out["target_groups_config"] = (
            aws_sdk_ec2.types.target_groups_config.deserialize_ec2_query(
                child_target_groups_config
            )
        )
    return out
