"""Generated from Smithy shape ``com.amazonaws.secretsmanager#GetRandomPasswordResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.random_password_type


class GetRandomPasswordResponse(TypedDict):
    random_password: NotRequired[
        "aws_sdk_secrets_manager.types.random_password_type.RandomPasswordType"
    ]
    """<p>A string with the password.</p>"""
