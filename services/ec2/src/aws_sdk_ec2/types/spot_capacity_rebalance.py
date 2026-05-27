"""Generated from Smithy shape ``com.amazonaws.ec2#SpotCapacityRebalance``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.replacement_strategy


class SpotCapacityRebalance(TypedDict):
    replacement_strategy: NotRequired[
        "aws_sdk_ec2.types.replacement_strategy.ReplacementStrategy"
    ]
    """<p>The replacement strategy to use. Only available for fleets of type <code>maintain</code>.</p> <p> <code>launch</code> - Spot Fleet launches a new replacement Spot Instance when a rebalance notification is emitted for an existing Spot Instance in the fleet. Spot Fleet does not terminate the instances that receive a rebalance notification. You can terminate the old instances, or you can leave them running. You are charged for all instances while they are running. </p> <p> <code>launch-before-terminate</code> - Spot Fleet launches a new replacement Spot Instance when a rebalance notification is emitted for an existing Spot Instance in the fleet, and then, after a delay that you specify (in <code>TerminationDelay</code>), terminates the instances that received a rebalance notification.</p>"""
    termination_delay: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The amount of time (in seconds) that Amazon EC2 waits before terminating the old Spot Instance after launching a new replacement Spot Instance.</p> <p>Required when <code>ReplacementStrategy</code> is set to <code>launch-before-terminate</code>.</p> <p>Not valid when <code>ReplacementStrategy</code> is set to <code>launch</code>.</p> <p>Valid values: Minimum value of <code>120</code> seconds. Maximum value of <code>7200</code> seconds.</p>"""
