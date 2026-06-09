"""Generated from Smithy shape ``com.amazonaws.ec2#FleetSpotCapacityRebalanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_replacement_strategy
    import aws_sdk_ec2.types.integer


class FleetSpotCapacityRebalanceRequest(TypedDict):
    replacement_strategy: NotRequired[
        "aws_sdk_ec2.types.fleet_replacement_strategy.FleetReplacementStrategy"
    ]
    """<p>The replacement strategy to use. Only available for fleets of type <code>maintain</code>.</p> <p> <code>launch</code> - EC2 Fleet launches a replacement Spot Instance when a rebalance notification is emitted for an existing Spot Instance in the fleet. EC2 Fleet does not terminate the instances that receive a rebalance notification. You can terminate the old instances, or you can leave them running. You are charged for all instances while they are running. </p> <p> <code>launch-before-terminate</code> - EC2 Fleet launches a replacement Spot Instance when a rebalance notification is emitted for an existing Spot Instance in the fleet, and then, after a delay that you specify (in <code>TerminationDelay</code>), terminates the instances that received a rebalance notification.</p>"""
    termination_delay: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The amount of time (in seconds) that Amazon EC2 waits before terminating the old Spot Instance after launching a new replacement Spot Instance.</p> <p>Required when <code>ReplacementStrategy</code> is set to <code>launch-before-terminate</code>.</p> <p>Not valid when <code>ReplacementStrategy</code> is set to <code>launch</code>.</p> <p>Valid values: Minimum value of <code>120</code> seconds. Maximum value of <code>7200</code> seconds.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetSpotCapacityRebalanceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replacement_strategy" in value:
        import aws_sdk_ec2.types.fleet_replacement_strategy

        aws_sdk_ec2.types.fleet_replacement_strategy.serialize_ec2_query(
            value["replacement_strategy"], pairs, f"{prefix}.ReplacementStrategy"
        )
    if "termination_delay" in value:
        pairs.append((f"{prefix}.TerminationDelay", str(value["termination_delay"])))


def deserialize_ec2_query(el: Element) -> FleetSpotCapacityRebalanceRequest:
    out: FleetSpotCapacityRebalanceRequest = {}  # type: ignore[typeddict-item]
    child_replacement_strategy = el.find("ReplacementStrategy")
    if child_replacement_strategy is not None:
        import aws_sdk_ec2.types.fleet_replacement_strategy

        out["replacement_strategy"] = (
            aws_sdk_ec2.types.fleet_replacement_strategy.deserialize_ec2_query(
                child_replacement_strategy
            )
        )
    child_termination_delay = el.find("TerminationDelay")
    if child_termination_delay is not None:
        out["termination_delay"] = int(child_termination_delay.text or "")
    return out
