"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_metering_payer_type
    import aws_sdk_ec2.types.transit_gateway_metering_policy_entry_state
    import aws_sdk_ec2.types.transit_gateway_metering_policy_rule


class TransitGatewayMeteringPolicyEntry(TypedDict):
    policy_rule_number: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The rule number of the metering policy entry.</p>"""
    metered_account: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_payer_type.TransitGatewayMeteringPayerType"
    ]
    """<p>The Amazon Web Services account ID to which the metered traffic is attributed.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_entry_state.TransitGatewayMeteringPolicyEntryState"
    ]
    """<p>The state of the metering policy entry.</p>"""
    updated_at: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the metering policy entry was last updated.</p>"""
    update_effective_at: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the metering policy entry update becomes effective.</p>"""
    metering_policy_rule: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_rule.TransitGatewayMeteringPolicyRule"
    ]
    """<p>The metering policy rule that defines traffic matching criteria.</p>"""
