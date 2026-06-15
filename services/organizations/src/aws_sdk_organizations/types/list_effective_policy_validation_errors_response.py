"""Generated from Smithy shape ``com.amazonaws.organizations#ListEffectivePolicyValidationErrorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.account_id
    import aws_sdk_organizations.types.effective_policy_type
    import aws_sdk_organizations.types.effective_policy_validation_errors
    import aws_sdk_organizations.types.next_token
    import aws_sdk_organizations.types.path
    import aws_sdk_organizations.types.timestamp


class ListEffectivePolicyValidationErrorsResponse(TypedDict):
    account_id: NotRequired["aws_sdk_organizations.types.account_id.AccountId"]
    """<p>The ID of the specified account.</p>"""
    policy_type: NotRequired[
        "aws_sdk_organizations.types.effective_policy_type.EffectivePolicyType"
    ]
    r"""<p>The specified policy type. One of the following values:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html\">DECLARATIVE_POLICY_EC2</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html\">BACKUP_POLICY</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html\">TAG_POLICY</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot.html\">CHATBOT_POLICY</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html\">AISERVICES_OPT_OUT_POLICY</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub.html\">SECURITYHUB_POLICY</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_upgrade_rollout.html\">UPGRADE_ROLLOUT_POLICY</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector.html\">INSPECTOR_POLICY</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock.html\">BEDROCK_POLICY</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3.html\">S3_POLICY</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director.html\">NETWORK_SECURITY_DIRECTOR_POLICY</a> </p> </li> </ul>"""
    path: NotRequired["aws_sdk_organizations.types.path.Path"]
    """<p>The path in the organization where the specified account exists.</p>"""
    evaluation_timestamp: NotRequired["aws_sdk_organizations.types.timestamp.Timestamp"]
    """<p>The time when the latest effective policy was generated for the specified account.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""
    effective_policy_validation_errors: NotRequired[
        "aws_sdk_organizations.types.effective_policy_validation_errors.EffectivePolicyValidationErrors"
    ]
    """<p>The <code>EffectivePolicyValidationError</code> object contains details about the validation errors that occurred when generating or enforcing an effective policy, such as which policies contributed to the error and location of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEffectivePolicyValidationErrorsResponse) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "policy_type" in value:
        import aws_sdk_organizations.types.effective_policy_type

        out["PolicyType"] = (
            aws_sdk_organizations.types.effective_policy_type.serialize_aws_json_1_1(
                value["policy_type"]
            )
        )
    if "path" in value:
        out["Path"] = value["path"]
    if "evaluation_timestamp" in value:
        import aws_sdk_organizations.types.timestamp

        out["EvaluationTimestamp"] = (
            aws_sdk_organizations.types.timestamp.serialize_aws_json_1_1(
                value["evaluation_timestamp"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "effective_policy_validation_errors" in value:
        import aws_sdk_organizations.types.effective_policy_validation_errors

        out["EffectivePolicyValidationErrors"] = (
            aws_sdk_organizations.types.effective_policy_validation_errors.serialize_aws_json_1_1(
                value["effective_policy_validation_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEffectivePolicyValidationErrorsResponse:
    out: ListEffectivePolicyValidationErrorsResponse = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "PolicyType" in data:
        import aws_sdk_organizations.types.effective_policy_type

        out["policy_type"] = (
            aws_sdk_organizations.types.effective_policy_type.deserialize_aws_json_1_1(
                data["PolicyType"]
            )
        )
    if "Path" in data:
        out["path"] = data["Path"]
    if "EvaluationTimestamp" in data:
        import aws_sdk_organizations.types.timestamp

        out["evaluation_timestamp"] = (
            aws_sdk_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["EvaluationTimestamp"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "EffectivePolicyValidationErrors" in data:
        import aws_sdk_organizations.types.effective_policy_validation_errors

        out["effective_policy_validation_errors"] = (
            aws_sdk_organizations.types.effective_policy_validation_errors.deserialize_aws_json_1_1(
                data["EffectivePolicyValidationErrors"]
            )
        )
    return out
