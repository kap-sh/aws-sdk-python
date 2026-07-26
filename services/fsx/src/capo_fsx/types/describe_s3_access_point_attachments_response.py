"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeS3AccessPointAttachmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.next_token
    import capo_fsx.types.s3_access_point_attachments


class DescribeS3AccessPointAttachmentsResponse(TypedDict, closed=True):
    s3_access_point_attachments: NotRequired[
        "capo_fsx.types.s3_access_point_attachments.S3AccessPointAttachments"
    ]
    """<p>Array of S3 access point attachments returned after a successful <code>DescribeS3AccessPointAttachments</code> operation.</p>"""
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeS3AccessPointAttachmentsResponse) -> dict:
    out: dict = {}
    if "s3_access_point_attachments" in value:
        import capo_fsx.types.s3_access_point_attachments

        out["S3AccessPointAttachments"] = (
            capo_fsx.types.s3_access_point_attachments.serialize_aws_json_1_1(
                value["s3_access_point_attachments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeS3AccessPointAttachmentsResponse:
    out: DescribeS3AccessPointAttachmentsResponse = {}  # type: ignore[typeddict-item]
    if "S3AccessPointAttachments" in data:
        import capo_fsx.types.s3_access_point_attachments

        out["s3_access_point_attachments"] = (
            capo_fsx.types.s3_access_point_attachments.deserialize_aws_json_1_1(
                data["S3AccessPointAttachments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
