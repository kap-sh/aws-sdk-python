"""Generated from Smithy shape ``com.amazonaws.pinpoint#ExportJobResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string


class ExportJobResource(TypedDict):
    role_arn: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorized Amazon Pinpoint to access the Amazon S3 location where the endpoint definitions were exported to.</p>"""
    s3_url_prefix: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL of the location in an Amazon Simple Storage Service (Amazon S3) bucket where the endpoint definitions were exported to. This location is typically a folder that contains multiple files. The URL should be in the following format: s3://<replaceable>bucket-name</replaceable>/<replaceable>folder-name</replaceable>/.</p>"""
    segment_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The identifier for the segment that the endpoint definitions were exported from. If this value isn't present, Amazon Pinpoint exported definitions for all the endpoints that are associated with the application.</p>"""
    segment_version: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The version of the segment that the endpoint definitions were exported from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportJobResource) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "s3_url_prefix" in value:
        out["S3UrlPrefix"] = value["s3_url_prefix"]
    if "segment_id" in value:
        out["SegmentId"] = value["segment_id"]
    if "segment_version" in value:
        out["SegmentVersion"] = value["segment_version"]
    return out


def deserialize_json(data: dict) -> ExportJobResource:
    out: ExportJobResource = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "S3UrlPrefix" in data:
        out["s3_url_prefix"] = data["S3UrlPrefix"]
    if "SegmentId" in data:
        out["segment_id"] = data["SegmentId"]
    if "SegmentVersion" in data:
        out["segment_version"] = data["SegmentVersion"]
    return out
