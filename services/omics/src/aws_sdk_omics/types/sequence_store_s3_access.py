"""Generated from Smithy shape ``com.amazonaws.omics#SequenceStoreS3Access``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.access_log_location
    import aws_sdk_omics.types.s3_access_point_arn
    import aws_sdk_omics.types.s3_uri


class SequenceStoreS3Access(TypedDict, closed=True):
    s3_uri: NotRequired["aws_sdk_omics.types.s3_uri.S3Uri"]
    """<p>The S3 URI of the sequence store.</p>"""
    s3_access_point_arn: NotRequired[
        "aws_sdk_omics.types.s3_access_point_arn.S3AccessPointArn"
    ]
    """<p>This is ARN of the access point associated with the S3 bucket storing read sets.</p>"""
    access_log_location: NotRequired[
        "aws_sdk_omics.types.access_log_location.AccessLogLocation"
    ]
    """<p>Location of the access logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SequenceStoreS3Access) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["s3Uri"] = value["s3_uri"]
    if "s3_access_point_arn" in value:
        out["s3AccessPointArn"] = value["s3_access_point_arn"]
    if "access_log_location" in value:
        out["accessLogLocation"] = value["access_log_location"]
    return out


def deserialize_json(data: dict) -> SequenceStoreS3Access:
    out: SequenceStoreS3Access = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    if "s3AccessPointArn" in data:
        out["s3_access_point_arn"] = data["s3AccessPointArn"]
    if "accessLogLocation" in data:
        out["access_log_location"] = data["accessLogLocation"]
    return out
