"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceNetworkPerformanceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_bandwidth_weighting
    import capo_ec2.types.instance_id


class ModifyInstanceNetworkPerformanceResult(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The instance ID that was updated.</p>"""
    bandwidth_weighting: NotRequired[
        "capo_ec2.types.instance_bandwidth_weighting.InstanceBandwidthWeighting"
    ]
    """<p>Contains the updated configuration for bandwidth weighting on the specified instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceNetworkPerformanceResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "bandwidth_weighting" in value:
        import capo_ec2.types.instance_bandwidth_weighting

        capo_ec2.types.instance_bandwidth_weighting.serialize_ec2_query(
            value["bandwidth_weighting"], pairs, f"{key_prefix}BandwidthWeighting"
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceNetworkPerformanceResult:
    out: ModifyInstanceNetworkPerformanceResult = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_bandwidth_weighting = el.find("BandwidthWeighting")
    if child_bandwidth_weighting is not None:
        import capo_ec2.types.instance_bandwidth_weighting

        out["bandwidth_weighting"] = (
            capo_ec2.types.instance_bandwidth_weighting.deserialize_ec2_query(
                child_bandwidth_weighting
            )
        )
    return out
