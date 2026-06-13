"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#S3ReportOutput``."""

from typing import TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError


class S3ReportOutput(TypedDict):
    s3_object_key: "str"
    """<p>The S3 object key for the generated report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ReportOutput) -> dict:
    out: dict = {}
    out["s3ObjectKey"] = value["s3_object_key"]
    return out


def deserialize_json(data: dict) -> S3ReportOutput:
    out: S3ReportOutput = {}  # type: ignore[typeddict-item]
    if "s3ObjectKey" in data:
        out["s3_object_key"] = data["s3ObjectKey"]
    else:
        raise DeserializationError("S3ReportOutput.s3_object_key required")
    return out
