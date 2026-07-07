"""Generated from Smithy shape ``com.amazonaws.mediaconvert#S3DestinationAccessControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.s3_object_canned_acl


class S3DestinationAccessControl(TypedDict, closed=True):
    canned_acl: NotRequired[
        "aws_sdk_mediaconvert.types.s3_object_canned_acl.S3ObjectCannedAcl"
    ]
    """Choose an Amazon S3 canned ACL for MediaConvert to apply to this output."""


# --- restJson1 ser/de ---
def serialize_json(value: S3DestinationAccessControl) -> dict:
    out: dict = {}
    if "canned_acl" in value:
        import aws_sdk_mediaconvert.types.s3_object_canned_acl

        out["cannedAcl"] = (
            aws_sdk_mediaconvert.types.s3_object_canned_acl.serialize_json(
                value["canned_acl"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3DestinationAccessControl:
    out: S3DestinationAccessControl = {}  # type: ignore[typeddict-item]
    if "cannedAcl" in data:
        import aws_sdk_mediaconvert.types.s3_object_canned_acl

        out["canned_acl"] = (
            aws_sdk_mediaconvert.types.s3_object_canned_acl.deserialize_json(
                data["cannedAcl"]
            )
        )
    return out
