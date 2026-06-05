"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkPerformanceOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_bandwidth_weighting


class InstanceNetworkPerformanceOptionsRequest(TypedDict):
    bandwidth_weighting: NotRequired[
        "aws_sdk_ec2.types.instance_bandwidth_weighting.InstanceBandwidthWeighting"
    ]
    """<p>Specify the bandwidth weighting option to boost the associated type of baseline bandwidth, as follows:</p> <dl> <dt>default</dt> <dd> <p>This option uses the standard bandwidth configuration for your instance type.</p> </dd> <dt>vpc-1</dt> <dd> <p>This option boosts your networking baseline bandwidth and reduces your EBS baseline bandwidth.</p> </dd> <dt>ebs-1</dt> <dd> <p>This option boosts your EBS baseline bandwidth and reduces your networking baseline bandwidth.</p> </dd> </dl>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceNetworkPerformanceOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "bandwidth_weighting" in value:
        import aws_sdk_ec2.types.instance_bandwidth_weighting

        aws_sdk_ec2.types.instance_bandwidth_weighting.serialize_ec2_query(
            value["bandwidth_weighting"], pairs, f"{prefix}.BandwidthWeighting"
        )


def deserialize_ec2_query(el: Element) -> InstanceNetworkPerformanceOptionsRequest:
    out: InstanceNetworkPerformanceOptionsRequest = {}  # type: ignore[typeddict-item]
    child_bandwidth_weighting = el.find("BandwidthWeighting")
    if child_bandwidth_weighting is not None:
        import aws_sdk_ec2.types.instance_bandwidth_weighting

        out["bandwidth_weighting"] = (
            aws_sdk_ec2.types.instance_bandwidth_weighting.deserialize_ec2_query(
                child_bandwidth_weighting
            )
        )
    return out
