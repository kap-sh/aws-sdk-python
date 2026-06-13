"""Generated from Smithy shape ``com.amazonaws.inspector2#Destination``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError


class Destination(TypedDict):
    bucket_name: "str"
    """<p>The name of the Amazon S3 bucket to export findings to.</p>"""
    key_prefix: NotRequired["str"]
    """<p>The prefix that the findings will be written under.</p>"""
    kms_key_arn: "str"
    """<p>The ARN of the KMS key used to encrypt data when exporting findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("Destination.bucket_name required")
    if "keyPrefix" in data:
        out["key_prefix"] = data["keyPrefix"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    else:
        raise DeserializationError("Destination.kms_key_arn required")
    return out
