"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateTrafficPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.accept_action
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.max_message_size_bytes
    import aws_sdk_mailmanager.types.policy_statement_list
    import aws_sdk_mailmanager.types.tag_list
    import aws_sdk_mailmanager.types.traffic_policy_name


class CreateTrafficPolicyRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    traffic_policy_name: (
        "aws_sdk_mailmanager.types.traffic_policy_name.TrafficPolicyName"
    )
    """<p>A user-friendly name for the traffic policy resource.</p>"""
    policy_statements: (
        "aws_sdk_mailmanager.types.policy_statement_list.PolicyStatementList"
    )
    """<p>Conditional statements for filtering email traffic.</p>"""
    default_action: "aws_sdk_mailmanager.types.accept_action.AcceptAction"
    """<p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>"""
    max_message_size_bytes: NotRequired[
        "aws_sdk_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
    ]
    """<p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>"""
    tags: NotRequired["aws_sdk_mailmanager.types.tag_list.TagList"]
    r"""<p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTrafficPolicyRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["TrafficPolicyName"] = value["traffic_policy_name"]
    import aws_sdk_mailmanager.types.policy_statement_list

    out["PolicyStatements"] = (
        aws_sdk_mailmanager.types.policy_statement_list.serialize_aws_json_1_0(
            value["policy_statements"]
        )
    )
    import aws_sdk_mailmanager.types.accept_action

    out["DefaultAction"] = (
        aws_sdk_mailmanager.types.accept_action.serialize_aws_json_1_0(
            value["default_action"]
        )
    )
    if "max_message_size_bytes" in value:
        out["MaxMessageSizeBytes"] = value["max_message_size_bytes"]
    if "tags" in value:
        import aws_sdk_mailmanager.types.tag_list

        out["Tags"] = aws_sdk_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateTrafficPolicyRequest:
    out: CreateTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "TrafficPolicyName" in data:
        out["traffic_policy_name"] = data["TrafficPolicyName"]
    else:
        raise DeserializationError(
            "CreateTrafficPolicyRequest.traffic_policy_name required"
        )
    if "PolicyStatements" in data:
        import aws_sdk_mailmanager.types.policy_statement_list

        out["policy_statements"] = (
            aws_sdk_mailmanager.types.policy_statement_list.deserialize_aws_json_1_0(
                data["PolicyStatements"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTrafficPolicyRequest.policy_statements required"
        )
    if "DefaultAction" in data:
        import aws_sdk_mailmanager.types.accept_action

        out["default_action"] = (
            aws_sdk_mailmanager.types.accept_action.deserialize_aws_json_1_0(
                data["DefaultAction"]
            )
        )
    else:
        raise DeserializationError("CreateTrafficPolicyRequest.default_action required")
    if "MaxMessageSizeBytes" in data:
        out["max_message_size_bytes"] = data["MaxMessageSizeBytes"]
    if "Tags" in data:
        import aws_sdk_mailmanager.types.tag_list

        out["tags"] = aws_sdk_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
