"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorSessionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_session


class CreateTrafficMirrorSessionResult(TypedDict):
    traffic_mirror_session: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_session.TrafficMirrorSession"
    ]
    """<p>Information about the Traffic Mirror session.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""
