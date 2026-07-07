"""Generated from Smithy shape ``com.amazonaws.appflow#S3InputFormatConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.s3_input_file_type


class S3InputFormatConfig(TypedDict, closed=True):
    s3_input_file_type: NotRequired[
        "aws_sdk_appflow.types.s3_input_file_type.S3InputFileType"
    ]
    """<p> The file type that Amazon AppFlow gets from your Amazon S3 bucket. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3InputFormatConfig) -> dict:
    out: dict = {}
    if "s3_input_file_type" in value:
        import aws_sdk_appflow.types.s3_input_file_type

        out["s3InputFileType"] = (
            aws_sdk_appflow.types.s3_input_file_type.serialize_json(
                value["s3_input_file_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3InputFormatConfig:
    out: S3InputFormatConfig = {}  # type: ignore[typeddict-item]
    if "s3InputFileType" in data:
        import aws_sdk_appflow.types.s3_input_file_type

        out["s3_input_file_type"] = (
            aws_sdk_appflow.types.s3_input_file_type.deserialize_json(
                data["s3InputFileType"]
            )
        )
    return out
