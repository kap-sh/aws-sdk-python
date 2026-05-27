"""Generated from Smithy shape ``com.amazonaws.ecs#IngressPathSummary``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.access_type
    import aws_sdk_ecs.types.string


class IngressPathSummary(TypedDict):
    access_type: "aws_sdk_ecs.types.access_type.AccessType"
    """<p>The type of access to the endpoint for the Express service.</p>"""
    endpoint: "aws_sdk_ecs.types.string.String"
    """<p>The endpoint for access to the service.</p>"""
