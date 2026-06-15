"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#UpdateRoutingControlStatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53_recovery_cluster.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_cluster.types.arns
    import aws_sdk_route53_recovery_cluster.types.update_routing_control_state_entries


class UpdateRoutingControlStatesRequest(TypedDict):
    update_routing_control_state_entries: "aws_sdk_route53_recovery_cluster.types.update_routing_control_state_entries.UpdateRoutingControlStateEntries"
    """<p>A set of routing control entries that you want to update.</p>"""
    safety_rules_to_override: NotRequired[
        "aws_sdk_route53_recovery_cluster.types.arns.Arns"
    ]
    r"""<p>The Amazon Resource Names (ARNs) for the safety rules that you want to override when you're updating routing control states. You can override one safety rule or multiple safety rules by including one or more ARNs, separated by commas.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html\"> Override safety rules to reroute traffic</a> in the Amazon Route 53 Application Recovery Controller Developer Guide.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRoutingControlStatesRequest) -> dict:
    out: dict = {}
    import aws_sdk_route53_recovery_cluster.types.update_routing_control_state_entries

    out["UpdateRoutingControlStateEntries"] = (
        aws_sdk_route53_recovery_cluster.types.update_routing_control_state_entries.serialize_aws_json_1_0(
            value["update_routing_control_state_entries"]
        )
    )
    if "safety_rules_to_override" in value:
        import aws_sdk_route53_recovery_cluster.types.arns

        out["SafetyRulesToOverride"] = (
            aws_sdk_route53_recovery_cluster.types.arns.serialize_aws_json_1_0(
                value["safety_rules_to_override"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRoutingControlStatesRequest:
    out: UpdateRoutingControlStatesRequest = {}  # type: ignore[typeddict-item]
    if "UpdateRoutingControlStateEntries" in data:
        import aws_sdk_route53_recovery_cluster.types.update_routing_control_state_entries

        out["update_routing_control_state_entries"] = (
            aws_sdk_route53_recovery_cluster.types.update_routing_control_state_entries.deserialize_aws_json_1_0(
                data["UpdateRoutingControlStateEntries"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRoutingControlStatesRequest.update_routing_control_state_entries required"
        )
    if "SafetyRulesToOverride" in data:
        import aws_sdk_route53_recovery_cluster.types.arns

        out["safety_rules_to_override"] = (
            aws_sdk_route53_recovery_cluster.types.arns.deserialize_aws_json_1_0(
                data["SafetyRulesToOverride"]
            )
        )
    return out
