"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#S3LogDeliveryDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__boolean
    import aws_sdk_kafkaconnect.types.__string


class S3LogDeliveryDescription(TypedDict):
    bucket: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The name of the S3 bucket that is the destination for log delivery.</p>"""
    enabled: "aws_sdk_kafkaconnect.types.__boolean.__boolean"
    """<p>Specifies whether connector logs get sent to the specified Amazon S3 destination.</p>"""
    prefix: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The S3 prefix that is the destination for log delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3LogDeliveryDescription) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    out["enabled"] = value.get("enabled", False)
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3LogDeliveryDescription:
    out: S3LogDeliveryDescription = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
