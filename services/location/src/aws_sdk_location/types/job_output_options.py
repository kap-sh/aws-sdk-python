"""Generated from Smithy shape ``com.amazonaws.location#JobOutputOptions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.job_output_format
    import aws_sdk_location.types.job_output_location


class JobOutputOptions(TypedDict):
    format: "aws_sdk_location.types.job_output_format.JobOutputFormat"
    """<p>Output data format. Currently only \"Parquet\" is supported.</p>"""
    location: "aws_sdk_location.types.job_output_location.JobOutputLocation"
    """<p>S3 ARN or URI where output files will be written.</p> <note> <p>The Amazon S3 bucket must exist in the same Amazon Web Services region where you plan to run your job.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobOutputOptions) -> dict:
    out: dict = {}
    out["Format"] = value["format"]
    out["Location"] = value["location"]
    return out


def deserialize_json(data: dict) -> JobOutputOptions:
    out: JobOutputOptions = {}  # type: ignore[typeddict-item]
    if "Format" in data:
        out["format"] = data["Format"]
    else:
        raise DeserializationError("JobOutputOptions.format required")
    if "Location" in data:
        out["location"] = data["Location"]
    else:
        raise DeserializationError("JobOutputOptions.location required")
    return out
