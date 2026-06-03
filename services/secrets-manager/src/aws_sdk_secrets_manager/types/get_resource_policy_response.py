"""Generated from Smithy shape ``com.amazonaws.secretsmanager#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.name_type
    import aws_sdk_secrets_manager.types.non_empty_resource_policy_type
    import aws_sdk_secrets_manager.types.secret_arn_type


class GetResourcePolicyResponse(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret that the resource-based policy was retrieved for.</p>"""
    name: NotRequired["aws_sdk_secrets_manager.types.name_type.NameType"]
    """<p>The name of the secret that the resource-based policy was retrieved for.</p>"""
    resource_policy: NotRequired[
        "aws_sdk_secrets_manager.types.non_empty_resource_policy_type.NonEmptyResourcePolicyType"
    ]
    """<p>A JSON-formatted string that contains the permissions policy attached to the secret. For more information about permissions policies, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html\">Authentication and access control for Secrets Manager</a>.</p>"""
