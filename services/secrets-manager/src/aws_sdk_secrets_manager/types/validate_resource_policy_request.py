"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ValidateResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.non_empty_resource_policy_type
    import aws_sdk_secrets_manager.types.secret_id_type


class ValidateResourcePolicyRequest(TypedDict):
    secret_id: NotRequired["aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"]
    """<p>The ARN or name of the secret with the resource-based policy you want to validate.</p>"""
    resource_policy: "aws_sdk_secrets_manager.types.non_empty_resource_policy_type.NonEmptyResourcePolicyType"
    """<p>A JSON-formatted string that contains an Amazon Web Services resource-based policy. The policy in the string identifies who can access or manage this secret and its versions. For example policies, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html\">Permissions policy examples</a>.</p>"""
