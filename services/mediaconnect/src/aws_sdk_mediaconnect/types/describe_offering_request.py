"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeOfferingRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.offering_arn


class DescribeOfferingRequest(TypedDict):
    offering_arn: "aws_sdk_mediaconnect.types.offering_arn.OfferingArn"
    """<p> The ARN of the offering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOfferingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeOfferingRequest:
    out: DescribeOfferingRequest = {}  # type: ignore[typeddict-item]
    return out
