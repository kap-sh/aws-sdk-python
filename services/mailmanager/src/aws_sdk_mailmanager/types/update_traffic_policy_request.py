"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateTrafficPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.accept_action
    import aws_sdk_mailmanager.types.max_message_size_bytes
    import aws_sdk_mailmanager.types.policy_statement_list
    import aws_sdk_mailmanager.types.traffic_policy_id
    import aws_sdk_mailmanager.types.traffic_policy_name


class UpdateTrafficPolicyRequest(TypedDict):
    traffic_policy_id: "aws_sdk_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    """<p>The identifier of the traffic policy that you want to update.</p>"""
    traffic_policy_name: NotRequired[
        "aws_sdk_mailmanager.types.traffic_policy_name.TrafficPolicyName"
    ]
    """<p>A user-friendly name for the traffic policy resource.</p>"""
    policy_statements: NotRequired[
        "aws_sdk_mailmanager.types.policy_statement_list.PolicyStatementList"
    ]
    """<p>The list of conditions to be updated for filtering email traffic.</p>"""
    default_action: NotRequired["aws_sdk_mailmanager.types.accept_action.AcceptAction"]
    """<p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>"""
    max_message_size_bytes: NotRequired[
        "aws_sdk_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
    ]
    """<p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTrafficPolicyRequest) -> dict:
    out: dict = {}
    out["TrafficPolicyId"] = value["traffic_policy_id"]
    if "traffic_policy_name" in value:
        out["TrafficPolicyName"] = value["traffic_policy_name"]
    if "policy_statements" in value:
        import aws_sdk_mailmanager.types.policy_statement_list

        out["PolicyStatements"] = (
            aws_sdk_mailmanager.types.policy_statement_list.serialize_aws_json_1_0(
                value["policy_statements"]
            )
        )
    if "default_action" in value:
        import aws_sdk_mailmanager.types.accept_action

        out["DefaultAction"] = (
            aws_sdk_mailmanager.types.accept_action.serialize_aws_json_1_0(
                value["default_action"]
            )
        )
    if "max_message_size_bytes" in value:
        out["MaxMessageSizeBytes"] = value["max_message_size_bytes"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTrafficPolicyRequest:
    out: UpdateTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
    if "TrafficPolicyId" in data:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    else:
        raise DeserializationError(
            "UpdateTrafficPolicyRequest.traffic_policy_id required"
        )
    if "TrafficPolicyName" in data:
        out["traffic_policy_name"] = data["TrafficPolicyName"]
    if "PolicyStatements" in data:
        import aws_sdk_mailmanager.types.policy_statement_list

        out["policy_statements"] = (
            aws_sdk_mailmanager.types.policy_statement_list.deserialize_aws_json_1_0(
                data["PolicyStatements"]
            )
        )
    if "DefaultAction" in data:
        import aws_sdk_mailmanager.types.accept_action

        out["default_action"] = (
            aws_sdk_mailmanager.types.accept_action.deserialize_aws_json_1_0(
                data["DefaultAction"]
            )
        )
    if "MaxMessageSizeBytes" in data:
        out["max_message_size_bytes"] = data["MaxMessageSizeBytes"]
    return out
