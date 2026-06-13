"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#GetKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudfront_keyvaluestore.types.key
    import aws_sdk_cloudfront_keyvaluestore.types.kvs_arn


class GetKeyRequest(TypedDict):
    kvs_arn: "aws_sdk_cloudfront_keyvaluestore.types.kvs_arn.KvsARN"
    """<p>The Amazon Resource Name (ARN) of the Key Value Store.</p>"""
    key: "aws_sdk_cloudfront_keyvaluestore.types.key.Key"
    """<p>The key to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKeyRequest:
    out: GetKeyRequest = {}  # type: ignore[typeddict-item]
    return out
