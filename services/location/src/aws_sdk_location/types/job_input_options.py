"""Generated from Smithy shape ``com.amazonaws.location#JobInputOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.job_input_format
    import aws_sdk_location.types.job_input_location


class JobInputOptions(TypedDict, closed=True):
    location: "aws_sdk_location.types.job_input_location.JobInputLocation"
    """<p>S3 ARN or URI where input files are stored.</p> <note> <p>The Amazon S3 bucket must be created in the same Amazon Web Services region where you plan to run your job.</p> </note>"""
    format: "aws_sdk_location.types.job_input_format.JobInputFormat"
    """<p>Input data format. Currently only <code>Parquet</code> is supported.</p> <note> <p>Input files have a limitation of 10gb per file, and 1gb per Parquet row-group within the file.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobInputOptions) -> dict:
    out: dict = {}
    out["Location"] = value["location"]
    out["Format"] = value["format"]
    return out


def deserialize_json(data: dict) -> JobInputOptions:
    out: JobInputOptions = {}  # type: ignore[typeddict-item]
    if "Location" in data:
        out["location"] = data["Location"]
    else:
        raise DeserializationError("JobInputOptions.location required")
    if "Format" in data:
        out["format"] = data["Format"]
    else:
        raise DeserializationError("JobInputOptions.format required")
    return out
