"""Generated from Smithy shape ``com.amazonaws.organizations#EffectivePolicyValidationError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.error_code
    import aws_sdk_organizations.types.error_message
    import aws_sdk_organizations.types.path_to_error
    import aws_sdk_organizations.types.policy_ids


class EffectivePolicyValidationError(TypedDict):
    error_code: NotRequired["aws_sdk_organizations.types.error_code.ErrorCode"]
    """<p>The error code for the validation error. For example, <code>ELEMENTS_TOO_MANY</code>.</p>"""
    error_message: NotRequired["aws_sdk_organizations.types.error_message.ErrorMessage"]
    """<p>The error message for the validation error.</p>"""
    path_to_error: NotRequired["aws_sdk_organizations.types.path_to_error.PathToError"]
    """<p>The path within the effective policy where the validation error occurred.</p>"""
    contributing_policies: NotRequired[
        "aws_sdk_organizations.types.policy_ids.PolicyIds"
    ]
    """<p>The individual policies <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.html\">inherited</a> and <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_attach.html\">attached</a> to the account which contributed to the validation error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EffectivePolicyValidationError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "path_to_error" in value:
        out["PathToError"] = value["path_to_error"]
    if "contributing_policies" in value:
        import aws_sdk_organizations.types.policy_ids

        out["ContributingPolicies"] = (
            aws_sdk_organizations.types.policy_ids.serialize_aws_json_1_1(
                value["contributing_policies"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EffectivePolicyValidationError:
    out: EffectivePolicyValidationError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "PathToError" in data:
        out["path_to_error"] = data["PathToError"]
    if "ContributingPolicies" in data:
        import aws_sdk_organizations.types.policy_ids

        out["contributing_policies"] = (
            aws_sdk_organizations.types.policy_ids.deserialize_aws_json_1_1(
                data["ContributingPolicies"]
            )
        )
    return out
