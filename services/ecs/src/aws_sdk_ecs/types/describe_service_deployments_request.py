"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServiceDeploymentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string_list


class DescribeServiceDeploymentsRequest(TypedDict):
    service_deployment_arns: "aws_sdk_ecs.types.string_list.StringList"
    """<p>The ARN of the service deployment.</p> <p>You can specify a maximum of 20 ARNs.</p>"""
