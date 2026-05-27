"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServiceRevisionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string_list


class DescribeServiceRevisionsRequest(TypedDict):
    service_revision_arns: "aws_sdk_ecs.types.string_list.StringList"
    """<p>The ARN of the service revision. </p> <p>You can specify a maximum of 20 ARNs.</p> <p>You can call <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html\">ListServiceDeployments</a> to get the ARNs.</p>"""
