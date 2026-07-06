"""Generated from Smithy shape ``com.amazonaws.omics#GetS3AccessPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.s3_access_point_arn


class GetS3AccessPolicyRequest(TypedDict, closed=True):
    s3_access_point_arn: "aws_sdk_omics.types.s3_access_point_arn.S3AccessPointArn"
    """<p>The S3 access point ARN that has the access policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetS3AccessPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetS3AccessPolicyRequest:
    out: GetS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
