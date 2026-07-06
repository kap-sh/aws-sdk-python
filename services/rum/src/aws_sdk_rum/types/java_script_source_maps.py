"""Generated from Smithy shape ``com.amazonaws.rum#JavaScriptSourceMaps``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rum.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rum.types.deobfuscation_s3_uri
    import aws_sdk_rum.types.deobfuscation_status


class JavaScriptSourceMaps(TypedDict, closed=True):
    status: "aws_sdk_rum.types.deobfuscation_status.DeobfuscationStatus"
    """<p> Specifies whether JavaScript error stack traces should be unminified for this app monitor. The default is for JavaScript error stack trace unminification to be <code>DISABLED</code>. </p>"""
    s3_uri: NotRequired["aws_sdk_rum.types.deobfuscation_s3_uri.DeobfuscationS3Uri"]
    """<p> The S3Uri of the bucket or folder that stores the source map files. It is required if status is ENABLED. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JavaScriptSourceMaps) -> dict:
    out: dict = {}
    out["Status"] = value["status"]
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> JavaScriptSourceMaps:
    out: JavaScriptSourceMaps = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("JavaScriptSourceMaps.status required")
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    return out
