"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLoadBalancersConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.classic_load_balancers


class ClassicLoadBalancersConfig(TypedDict, closed=True):
    classic_load_balancers: NotRequired[
        "capo_ec2.types.classic_load_balancers.ClassicLoadBalancers"
    ]
    """<p>One or more Classic Load Balancers.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClassicLoadBalancersConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "classic_load_balancers" in value:
        import capo_ec2.types.classic_load_balancers

        capo_ec2.types.classic_load_balancers.serialize_ec2_query(
            value["classic_load_balancers"], pairs, f"{key_prefix}ClassicLoadBalancers"
        )


def deserialize_ec2_query(el: Element) -> ClassicLoadBalancersConfig:
    out: ClassicLoadBalancersConfig = {}  # type: ignore[typeddict-item]
    if el.find("ClassicLoadBalancers") is not None:
        import capo_ec2.types.classic_load_balancers

        out["classic_load_balancers"] = (
            capo_ec2.types.classic_load_balancers.deserialize_ec2_query(
                el, "ClassicLoadBalancers"
            )
        )
    return out
