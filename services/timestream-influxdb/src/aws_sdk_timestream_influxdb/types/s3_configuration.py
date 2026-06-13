"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#S3Configuration``."""

from typing import TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError


class S3Configuration(TypedDict):
    bucket_name: "str"
    """<p>The name of the S3 bucket to deliver logs to.</p>"""
    enabled: "bool"
    """<p>Indicates whether log delivery to the S3 bucket is enabled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Configuration) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("S3Configuration.bucket_name required")
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        raise DeserializationError("S3Configuration.enabled required")
    return out
