"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetTrafficPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.accept_action
    import aws_sdk_mailmanager.types.max_message_size_bytes
    import aws_sdk_mailmanager.types.policy_statement_list
    import aws_sdk_mailmanager.types.traffic_policy_arn
    import aws_sdk_mailmanager.types.traffic_policy_id
    import aws_sdk_mailmanager.types.traffic_policy_name


class GetTrafficPolicyResponse(TypedDict):
    traffic_policy_name: (
        "aws_sdk_mailmanager.types.traffic_policy_name.TrafficPolicyName"
    )
    """<p>A user-friendly name for the traffic policy resource.</p>"""
    traffic_policy_id: "aws_sdk_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    """<p>The identifier of the traffic policy resource.</p>"""
    traffic_policy_arn: NotRequired[
        "aws_sdk_mailmanager.types.traffic_policy_arn.TrafficPolicyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the traffic policy resource.</p>"""
    policy_statements: NotRequired[
        "aws_sdk_mailmanager.types.policy_statement_list.PolicyStatementList"
    ]
    """<p>The list of conditions which are in the traffic policy resource.</p>"""
    max_message_size_bytes: NotRequired[
        "aws_sdk_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
    ]
    """<p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>"""
    default_action: NotRequired["aws_sdk_mailmanager.types.accept_action.AcceptAction"]
    """<p>The default action of the traffic policy.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the traffic policy was created.</p>"""
    last_updated_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the traffic policy was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTrafficPolicyResponse) -> dict:
    out: dict = {}
    out["TrafficPolicyName"] = value["traffic_policy_name"]
    out["TrafficPolicyId"] = value["traffic_policy_id"]
    if "traffic_policy_arn" in value:
        out["TrafficPolicyArn"] = value["traffic_policy_arn"]
    if "policy_statements" in value:
        import aws_sdk_mailmanager.types.policy_statement_list

        out["PolicyStatements"] = (
            aws_sdk_mailmanager.types.policy_statement_list.serialize_aws_json_1_0(
                value["policy_statements"]
            )
        )
    if "max_message_size_bytes" in value:
        out["MaxMessageSizeBytes"] = value["max_message_size_bytes"]
    if "default_action" in value:
        import aws_sdk_mailmanager.types.accept_action

        out["DefaultAction"] = (
            aws_sdk_mailmanager.types.accept_action.serialize_aws_json_1_0(
                value["default_action"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["LastUpdatedTimestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTrafficPolicyResponse:
    out: GetTrafficPolicyResponse = {}  # type: ignore[typeddict-item]
    if "TrafficPolicyName" in data:
        out["traffic_policy_name"] = data["TrafficPolicyName"]
    else:
        raise DeserializationError(
            "GetTrafficPolicyResponse.traffic_policy_name required"
        )
    if "TrafficPolicyId" in data:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    else:
        raise DeserializationError(
            "GetTrafficPolicyResponse.traffic_policy_id required"
        )
    if "TrafficPolicyArn" in data:
        out["traffic_policy_arn"] = data["TrafficPolicyArn"]
    if "PolicyStatements" in data:
        import aws_sdk_mailmanager.types.policy_statement_list

        out["policy_statements"] = (
            aws_sdk_mailmanager.types.policy_statement_list.deserialize_aws_json_1_0(
                data["PolicyStatements"]
            )
        )
    if "MaxMessageSizeBytes" in data:
        out["max_message_size_bytes"] = data["MaxMessageSizeBytes"]
    if "DefaultAction" in data:
        import aws_sdk_mailmanager.types.accept_action

        out["default_action"] = (
            aws_sdk_mailmanager.types.accept_action.deserialize_aws_json_1_0(
                data["DefaultAction"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTimestamp"]
            )
        )
    return out
