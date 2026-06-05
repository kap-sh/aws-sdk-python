"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceNetworkPerformanceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_bandwidth_weighting
    import aws_sdk_ec2.types.instance_id


class ModifyInstanceNetworkPerformanceRequest(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance to update.</p>"""
    bandwidth_weighting: NotRequired[
        "aws_sdk_ec2.types.instance_bandwidth_weighting.InstanceBandwidthWeighting"
    ]
    """<p>Specify the bandwidth weighting option to boost the associated type of baseline bandwidth, as follows:</p> <dl> <dt>default</dt> <dd> <p>This option uses the standard bandwidth configuration for your instance type.</p> </dd> <dt>vpc-1</dt> <dd> <p>This option boosts your networking baseline bandwidth and reduces your EBS baseline bandwidth.</p> </dd> <dt>ebs-1</dt> <dd> <p>This option boosts your EBS baseline bandwidth and reduces your networking baseline bandwidth.</p> </dd> </dl>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceNetworkPerformanceRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "bandwidth_weighting" in value:
        import aws_sdk_ec2.types.instance_bandwidth_weighting

        aws_sdk_ec2.types.instance_bandwidth_weighting.serialize_ec2_query(
            value["bandwidth_weighting"], pairs, f"{prefix}.BandwidthWeighting"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyInstanceNetworkPerformanceRequest:
    out: ModifyInstanceNetworkPerformanceRequest = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_bandwidth_weighting = el.find("BandwidthWeighting")
    if child_bandwidth_weighting is not None:
        import aws_sdk_ec2.types.instance_bandwidth_weighting

        out["bandwidth_weighting"] = (
            aws_sdk_ec2.types.instance_bandwidth_weighting.deserialize_ec2_query(
                child_bandwidth_weighting
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
