"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteExpressGatewayServiceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeleteExpressGatewayServiceRequest(TypedDict):
    service_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Express service to delete. The ARN uniquely identifies the service within your Amazon Web Services account and region.</p>"""
