"""Generated from Smithy shape ``com.amazonaws.omics#DeleteS3AccessPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.s3_access_point_arn


class DeleteS3AccessPolicyRequest(TypedDict):
    s3_access_point_arn: "aws_sdk_omics.types.s3_access_point_arn.S3AccessPointArn"
    """<p>The S3 access point ARN that has the access policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteS3AccessPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteS3AccessPolicyRequest:
    out: DeleteS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
