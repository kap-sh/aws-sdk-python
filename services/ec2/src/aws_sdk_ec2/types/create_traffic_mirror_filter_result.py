"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorFilterResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_filter


class CreateTrafficMirrorFilterResult(TypedDict):
    traffic_mirror_filter: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter.TrafficMirrorFilter"
    ]
    """<p>Information about the Traffic Mirror filter.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""
