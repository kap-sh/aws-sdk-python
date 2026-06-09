"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLoadBalancersConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.classic_load_balancers


class ClassicLoadBalancersConfig(TypedDict):
    classic_load_balancers: NotRequired[
        "aws_sdk_ec2.types.classic_load_balancers.ClassicLoadBalancers"
    ]
    """<p>One or more Classic Load Balancers.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClassicLoadBalancersConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "classic_load_balancers" in value:
        import aws_sdk_ec2.types.classic_load_balancers

        aws_sdk_ec2.types.classic_load_balancers.serialize_ec2_query(
            value["classic_load_balancers"], pairs, f"{prefix}.ClassicLoadBalancers"
        )


def deserialize_ec2_query(el: Element) -> ClassicLoadBalancersConfig:
    out: ClassicLoadBalancersConfig = {}  # type: ignore[typeddict-item]
    if el.find("ClassicLoadBalancers") is not None:
        import aws_sdk_ec2.types.classic_load_balancers

        out["classic_load_balancers"] = (
            aws_sdk_ec2.types.classic_load_balancers.deserialize_ec2_query(
                el, "ClassicLoadBalancers"
            )
        )
    return out
