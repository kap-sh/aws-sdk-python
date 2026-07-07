"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#PutKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront_keyvaluestore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront_keyvaluestore.types.etag
    import aws_sdk_cloudfront_keyvaluestore.types.key
    import aws_sdk_cloudfront_keyvaluestore.types.kvs_arn
    import aws_sdk_cloudfront_keyvaluestore.types.value


class PutKeyRequest(TypedDict, closed=True):
    key: "aws_sdk_cloudfront_keyvaluestore.types.key.Key"
    """<p>The key to put.</p>"""
    value: "aws_sdk_cloudfront_keyvaluestore.types.value.Value"
    """<p>The value to put.</p>"""
    kvs_arn: "aws_sdk_cloudfront_keyvaluestore.types.kvs_arn.KvsARN"
    """<p>The Amazon Resource Name (ARN) of the Key Value Store.</p>"""
    if_match: "aws_sdk_cloudfront_keyvaluestore.types.etag.Etag"
    """<p>The current version (ETag) of the Key Value Store that you are putting keys into, which you can get using DescribeKeyValueStore.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutKeyRequest) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> PutKeyRequest:
    out: PutKeyRequest = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("PutKeyRequest.value required")
    return out
