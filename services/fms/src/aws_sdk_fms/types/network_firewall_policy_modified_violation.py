"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallPolicyModifiedViolation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.network_firewall_policy_description
    import aws_sdk_fms.types.violation_target


class NetworkFirewallPolicyModifiedViolation(TypedDict):
    violation_target: NotRequired["aws_sdk_fms.types.violation_target.ViolationTarget"]
    """<p>The ID of the Network Firewall or VPC resource that's in violation.</p>"""
    current_policy_description: NotRequired[
        "aws_sdk_fms.types.network_firewall_policy_description.NetworkFirewallPolicyDescription"
    ]
    """<p>The policy that's currently in use in the individual account. </p>"""
    expected_policy_description: NotRequired[
        "aws_sdk_fms.types.network_firewall_policy_description.NetworkFirewallPolicyDescription"
    ]
    """<p>The policy that should be in use in the individual account in order to be compliant. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkFirewallPolicyModifiedViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "current_policy_description" in value:
        import aws_sdk_fms.types.network_firewall_policy_description

        out["CurrentPolicyDescription"] = (
            aws_sdk_fms.types.network_firewall_policy_description.serialize_aws_json_1_1(
                value["current_policy_description"]
            )
        )
    if "expected_policy_description" in value:
        import aws_sdk_fms.types.network_firewall_policy_description

        out["ExpectedPolicyDescription"] = (
            aws_sdk_fms.types.network_firewall_policy_description.serialize_aws_json_1_1(
                value["expected_policy_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkFirewallPolicyModifiedViolation:
    out: NetworkFirewallPolicyModifiedViolation = {}  # type: ignore[typeddict-item]
    if "ViolationTarget" in data:
        out["violation_target"] = data["ViolationTarget"]
    if "CurrentPolicyDescription" in data:
        import aws_sdk_fms.types.network_firewall_policy_description

        out["current_policy_description"] = (
            aws_sdk_fms.types.network_firewall_policy_description.deserialize_aws_json_1_1(
                data["CurrentPolicyDescription"]
            )
        )
    if "ExpectedPolicyDescription" in data:
        import aws_sdk_fms.types.network_firewall_policy_description

        out["expected_policy_description"] = (
            aws_sdk_fms.types.network_firewall_policy_description.deserialize_aws_json_1_1(
                data["ExpectedPolicyDescription"]
            )
        )
    return out
