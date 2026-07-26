"""Generated from Smithy shape ``com.amazonaws.transfer#FileLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.efs_file_location
    import capo_transfer.types.s3_file_location


class FileLocation(TypedDict, closed=True):
    s3_file_location: NotRequired["capo_transfer.types.s3_file_location.S3FileLocation"]
    """<p>Specifies the S3 details for the file being used, such as bucket, ETag, and so forth.</p>"""
    efs_file_location: NotRequired[
        "capo_transfer.types.efs_file_location.EfsFileLocation"
    ]
    """<p>Specifies the Amazon EFS identifier and the path for the file being used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileLocation) -> dict:
    out: dict = {}
    if "s3_file_location" in value:
        import capo_transfer.types.s3_file_location

        out["S3FileLocation"] = (
            capo_transfer.types.s3_file_location.serialize_aws_json_1_1(
                value["s3_file_location"]
            )
        )
    if "efs_file_location" in value:
        import capo_transfer.types.efs_file_location

        out["EfsFileLocation"] = (
            capo_transfer.types.efs_file_location.serialize_aws_json_1_1(
                value["efs_file_location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileLocation:
    out: FileLocation = {}  # type: ignore[typeddict-item]
    if "S3FileLocation" in data:
        import capo_transfer.types.s3_file_location

        out["s3_file_location"] = (
            capo_transfer.types.s3_file_location.deserialize_aws_json_1_1(
                data["S3FileLocation"]
            )
        )
    if "EfsFileLocation" in data:
        import capo_transfer.types.efs_file_location

        out["efs_file_location"] = (
            capo_transfer.types.efs_file_location.deserialize_aws_json_1_1(
                data["EfsFileLocation"]
            )
        )
    return out
