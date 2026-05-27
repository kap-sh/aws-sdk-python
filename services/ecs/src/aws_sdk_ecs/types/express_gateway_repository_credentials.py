"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayRepositoryCredentials``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ExpressGatewayRepositoryCredentials(TypedDict):
    credentials_parameter: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secret containing the private repository credentials.</p>"""
