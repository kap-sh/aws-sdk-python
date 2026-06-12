"""Generated from Smithy shape ``com.amazonaws.configservice#CustomPolicyDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.boolean
    import aws_sdk_config_service.types.policy_runtime
    import aws_sdk_config_service.types.policy_text


class CustomPolicyDetails(TypedDict):
    policy_runtime: "aws_sdk_config_service.types.policy_runtime.PolicyRuntime"
    """<p>The runtime system for your Config Custom Policy rule. Guard is a policy-as-code language that allows you to write policies that are enforced by Config Custom Policy rules. For more information about Guard, see the <a href=\"https://github.com/aws-cloudformation/cloudformation-guard\">Guard GitHub Repository</a>.</p>"""
    policy_text: "aws_sdk_config_service.types.policy_text.PolicyText"
    """<p>The policy definition containing the logic for your Config Custom Policy rule.</p>"""
    enable_debug_log_delivery: "aws_sdk_config_service.types.boolean.Boolean"
    """<p>The boolean expression for enabling debug logging for your Config Custom Policy rule. The default value is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomPolicyDetails) -> dict:
    out: dict = {}
    out["PolicyRuntime"] = value["policy_runtime"]
    out["PolicyText"] = value["policy_text"]
    out["EnableDebugLogDelivery"] = value.get("enable_debug_log_delivery", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomPolicyDetails:
    out: CustomPolicyDetails = {}  # type: ignore[typeddict-item]
    if "PolicyRuntime" in data:
        out["policy_runtime"] = data["PolicyRuntime"]
    else:
        raise DeserializationError("CustomPolicyDetails.policy_runtime required")
    if "PolicyText" in data:
        out["policy_text"] = data["PolicyText"]
    else:
        raise DeserializationError("CustomPolicyDetails.policy_text required")
    if "EnableDebugLogDelivery" in data:
        out["enable_debug_log_delivery"] = data["EnableDebugLogDelivery"]
    else:
        out["enable_debug_log_delivery"] = False
    return out
