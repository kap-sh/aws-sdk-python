"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_metering_payer_type
    import capo_ec2.types.transit_gateway_metering_policy_entry_state
    import capo_ec2.types.transit_gateway_metering_policy_rule


class TransitGatewayMeteringPolicyEntry(TypedDict, closed=True):
    policy_rule_number: NotRequired["capo_ec2.types.string.String"]
    """<p>The rule number of the metering policy entry.</p>"""
    metered_account: NotRequired[
        "capo_ec2.types.transit_gateway_metering_payer_type.TransitGatewayMeteringPayerType"
    ]
    """<p>The Amazon Web Services account ID to which the metered traffic is attributed.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_metering_policy_entry_state.TransitGatewayMeteringPolicyEntryState"
    ]
    """<p>The state of the metering policy entry.</p>"""
    updated_at: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time when the metering policy entry was last updated.</p>"""
    update_effective_at: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the metering policy entry update becomes effective.</p>"""
    metering_policy_rule: NotRequired[
        "capo_ec2.types.transit_gateway_metering_policy_rule.TransitGatewayMeteringPolicyRule"
    ]
    """<p>The metering policy rule that defines traffic matching criteria.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMeteringPolicyEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "policy_rule_number" in value:
        pairs.append(
            (f"{key_prefix}PolicyRuleNumber", str(value["policy_rule_number"]))
        )
    if "metered_account" in value:
        import capo_ec2.types.transit_gateway_metering_payer_type

        capo_ec2.types.transit_gateway_metering_payer_type.serialize_ec2_query(
            value["metered_account"], pairs, f"{key_prefix}MeteredAccount"
        )
    if "state" in value:
        import capo_ec2.types.transit_gateway_metering_policy_entry_state

        capo_ec2.types.transit_gateway_metering_policy_entry_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "updated_at" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["updated_at"], pairs, f"{key_prefix}UpdatedAt"
        )
    if "update_effective_at" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["update_effective_at"], pairs, f"{key_prefix}UpdateEffectiveAt"
        )
    if "metering_policy_rule" in value:
        import capo_ec2.types.transit_gateway_metering_policy_rule

        capo_ec2.types.transit_gateway_metering_policy_rule.serialize_ec2_query(
            value["metering_policy_rule"], pairs, f"{key_prefix}MeteringPolicyRule"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayMeteringPolicyEntry:
    out: TransitGatewayMeteringPolicyEntry = {}  # type: ignore[typeddict-item]
    child_policy_rule_number = el.find("policyRuleNumber")
    if child_policy_rule_number is not None:
        out["policy_rule_number"] = str(child_policy_rule_number.text or "")
    child_metered_account = el.find("meteredAccount")
    if child_metered_account is not None:
        import capo_ec2.types.transit_gateway_metering_payer_type

        out["metered_account"] = (
            capo_ec2.types.transit_gateway_metering_payer_type.deserialize_ec2_query(
                child_metered_account
            )
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_metering_policy_entry_state

        out["state"] = (
            capo_ec2.types.transit_gateway_metering_policy_entry_state.deserialize_ec2_query(
                child_state
            )
        )
    child_updated_at = el.find("updatedAt")
    if child_updated_at is not None:
        import capo_ec2.types.millisecond_date_time

        out["updated_at"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_updated_at
        )
    child_update_effective_at = el.find("updateEffectiveAt")
    if child_update_effective_at is not None:
        import capo_ec2.types.millisecond_date_time

        out["update_effective_at"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_update_effective_at
            )
        )
    child_metering_policy_rule = el.find("meteringPolicyRule")
    if child_metering_policy_rule is not None:
        import capo_ec2.types.transit_gateway_metering_policy_rule

        out["metering_policy_rule"] = (
            capo_ec2.types.transit_gateway_metering_policy_rule.deserialize_ec2_query(
                child_metering_policy_rule
            )
        )
    return out
