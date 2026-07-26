"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateNetworkPerformanceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_bandwidth_weighting


class LaunchTemplateNetworkPerformanceOptions(TypedDict, closed=True):
    bandwidth_weighting: NotRequired[
        "capo_ec2.types.instance_bandwidth_weighting.InstanceBandwidthWeighting"
    ]
    """<p>When you configure network bandwidth weighting, you can boost baseline bandwidth for either networking or EBS by up to 25%. The total available baseline bandwidth for your instance remains the same. The default option uses the standard bandwidth configuration for your instance type.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateNetworkPerformanceOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "bandwidth_weighting" in value:
        import capo_ec2.types.instance_bandwidth_weighting

        capo_ec2.types.instance_bandwidth_weighting.serialize_ec2_query(
            value["bandwidth_weighting"], pairs, f"{prefix}.BandwidthWeighting"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateNetworkPerformanceOptions:
    out: LaunchTemplateNetworkPerformanceOptions = {}  # type: ignore[typeddict-item]
    child_bandwidth_weighting = el.find("BandwidthWeighting")
    if child_bandwidth_weighting is not None:
        import capo_ec2.types.instance_bandwidth_weighting

        out["bandwidth_weighting"] = (
            capo_ec2.types.instance_bandwidth_weighting.deserialize_ec2_query(
                child_bandwidth_weighting
            )
        )
    return out
