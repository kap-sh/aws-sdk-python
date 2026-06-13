"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#S3ReportOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class S3ReportOutput(TypedDict):
    s3_object_key: NotRequired["str"]
    """<p>The S3 object key where the generated report is stored.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3ReportOutput) -> dict:
    out: dict = {}
    if "s3_object_key" in value:
        out["s3ObjectKey"] = value["s3_object_key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3ReportOutput:
    out: S3ReportOutput = {}  # type: ignore[typeddict-item]
    if "s3ObjectKey" in data:
        out["s3_object_key"] = data["s3ObjectKey"]
    return out
