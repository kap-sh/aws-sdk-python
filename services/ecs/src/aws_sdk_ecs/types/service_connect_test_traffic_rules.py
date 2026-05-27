"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectTestTrafficRules``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_connect_test_traffic_header_rules


class ServiceConnectTestTrafficRules(TypedDict):
    header: "aws_sdk_ecs.types.service_connect_test_traffic_header_rules.ServiceConnectTestTrafficHeaderRules"
    """<p>The HTTP header-based routing rules that determine which requests should be routed to the new service version during blue/green deployment testing. These rules provide fine-grained control over test traffic routing based on request headers.</p>"""
