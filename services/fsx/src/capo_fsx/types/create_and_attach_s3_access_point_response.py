"""Generated from Smithy shape ``com.amazonaws.fsx#CreateAndAttachS3AccessPointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.s3_access_point_attachment


class CreateAndAttachS3AccessPointResponse(TypedDict, closed=True):
    s3_access_point_attachment: NotRequired[
        "capo_fsx.types.s3_access_point_attachment.S3AccessPointAttachment"
    ]
    """<p>Describes the configuration of the S3 access point created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAndAttachS3AccessPointResponse) -> dict:
    out: dict = {}
    if "s3_access_point_attachment" in value:
        import capo_fsx.types.s3_access_point_attachment

        out["S3AccessPointAttachment"] = (
            capo_fsx.types.s3_access_point_attachment.serialize_aws_json_1_1(
                value["s3_access_point_attachment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAndAttachS3AccessPointResponse:
    out: CreateAndAttachS3AccessPointResponse = {}  # type: ignore[typeddict-item]
    if "S3AccessPointAttachment" in data:
        import capo_fsx.types.s3_access_point_attachment

        out["s3_access_point_attachment"] = (
            capo_fsx.types.s3_access_point_attachment.deserialize_aws_json_1_1(
                data["S3AccessPointAttachment"]
            )
        )
    return out
