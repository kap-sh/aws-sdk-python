"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectTestTrafficHeaderMatchRules``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ServiceConnectTestTrafficHeaderMatchRules(TypedDict):
    exact: "aws_sdk_ecs.types.string.String"
    """<p>The exact value that the HTTP header must match for the test traffic routing rule to apply. This provides precise control over which requests are routed to the new service revision during blue/green deployments.</p>"""
