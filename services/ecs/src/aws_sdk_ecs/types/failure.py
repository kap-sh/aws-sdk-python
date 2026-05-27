"""Generated from Smithy shape ``com.amazonaws.ecs#Failure``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class Failure(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the failed resource.</p>"""
    reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason for the failure.</p>"""
    detail: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The details of the failure.</p>"""
