"""Generated from Smithy shape ``com.amazonaws.transfer#S3Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.s3_tag_key
    import aws_sdk_transfer.types.s3_tag_value


class S3Tag(TypedDict):
    key: "aws_sdk_transfer.types.s3_tag_key.S3TagKey"
    """<p>The name assigned to the tag that you create.</p>"""
    value: "aws_sdk_transfer.types.s3_tag_value.S3TagValue"
    """<p>The value that corresponds to the key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Tag:
    out: S3Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("S3Tag.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("S3Tag.value required")
    return out
