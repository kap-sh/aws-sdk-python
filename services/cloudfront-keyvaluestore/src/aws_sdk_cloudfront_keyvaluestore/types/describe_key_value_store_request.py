"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#DescribeKeyValueStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_cloudfront_keyvaluestore.types.kvs_arn

class DescribeKeyValueStoreRequest(TypedDict):
    kvs_arn: "aws_sdk_cloudfront_keyvaluestore.types.kvs_arn.KvsARN"
    """<p>The Amazon Resource Name (ARN) of the Key Value Store.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeKeyValueStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeKeyValueStoreRequest:
    out: DescribeKeyValueStoreRequest = {}  # type: ignore[typeddict-item]
    return out