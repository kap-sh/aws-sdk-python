"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#DeleteKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.etag
    import capo_cloudfront_keyvaluestore.types.key
    import capo_cloudfront_keyvaluestore.types.kvs_arn


class DeleteKeyRequest(TypedDict, closed=True):
    kvs_arn: "capo_cloudfront_keyvaluestore.types.kvs_arn.KvsARN"
    """<p>The Amazon Resource Name (ARN) of the Key Value Store.</p>"""
    key: "capo_cloudfront_keyvaluestore.types.key.Key"
    """<p>The key to delete.</p>"""
    if_match: "capo_cloudfront_keyvaluestore.types.etag.Etag"
    """<p>The current version (ETag) of the Key Value Store that you are deleting keys from, which you can get using DescribeKeyValueStore.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKeyRequest:
    out: DeleteKeyRequest = {}  # type: ignore[typeddict-item]
    return out
