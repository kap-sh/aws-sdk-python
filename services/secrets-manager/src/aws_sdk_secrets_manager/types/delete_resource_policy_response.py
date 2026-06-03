"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DeleteResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.name_type
    import aws_sdk_secrets_manager.types.secret_arn_type


class DeleteResourcePolicyResponse(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret that the resource-based policy was deleted for.</p>"""
    name: NotRequired["aws_sdk_secrets_manager.types.name_type.NameType"]
    """<p>The name of the secret that the resource-based policy was deleted for.</p>"""
