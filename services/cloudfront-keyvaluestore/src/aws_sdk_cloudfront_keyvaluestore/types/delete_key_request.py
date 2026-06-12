"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#DeleteKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_cloudfront_keyvaluestore.types.etag
    import aws_sdk_cloudfront_keyvaluestore.types.key
    import aws_sdk_cloudfront_keyvaluestore.types.kvs_arn

class DeleteKeyRequest(TypedDict):
    kvs_arn: "aws_sdk_cloudfront_keyvaluestore.types.kvs_arn.KvsARN"
    """<p>The Amazon Resource Name (ARN) of the Key Value Store.</p>"""
    key: "aws_sdk_cloudfront_keyvaluestore.types.key.Key"
    """<p>The key to delete.</p>"""
    if_match: "aws_sdk_cloudfront_keyvaluestore.types.etag.Etag"
    """<p>The current version (ETag) of the Key Value Store that you are deleting keys from, which you can get using DescribeKeyValueStore.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKeyRequest:
    out: DeleteKeyRequest = {}  # type: ignore[typeddict-item]
    return out