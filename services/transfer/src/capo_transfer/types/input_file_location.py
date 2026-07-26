"""Generated from Smithy shape ``com.amazonaws.transfer#InputFileLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.efs_file_location
    import capo_transfer.types.s3_input_file_location


class InputFileLocation(TypedDict, closed=True):
    s3_file_location: NotRequired[
        "capo_transfer.types.s3_input_file_location.S3InputFileLocation"
    ]
    """<p>Specifies the details for the Amazon S3 file that's being copied or decrypted.</p>"""
    efs_file_location: NotRequired[
        "capo_transfer.types.efs_file_location.EfsFileLocation"
    ]
    """<p>Specifies the details for the Amazon Elastic File System (Amazon EFS) file that's being decrypted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputFileLocation) -> dict:
    out: dict = {}
    if "s3_file_location" in value:
        import capo_transfer.types.s3_input_file_location

        out["S3FileLocation"] = (
            capo_transfer.types.s3_input_file_location.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> InputFileLocation:
    out: InputFileLocation = {}  # type: ignore[typeddict-item]
    if "S3FileLocation" in data:
        import capo_transfer.types.s3_input_file_location

        out["s3_file_location"] = (
            capo_transfer.types.s3_input_file_location.deserialize_aws_json_1_1(
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
