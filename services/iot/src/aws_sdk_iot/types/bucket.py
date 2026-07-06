"""Generated from Smithy shape ``com.amazonaws.iot#Bucket``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.bucket_key_value
    import aws_sdk_iot.types.count


class Bucket(TypedDict, closed=True):
    key_value: NotRequired["aws_sdk_iot.types.bucket_key_value.BucketKeyValue"]
    """<p>The value counted for the particular bucket.</p>"""
    count: "aws_sdk_iot.types.count.Count"
    """<p>The number of documents that have the value counted for the particular bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Bucket) -> dict:
    out: dict = {}
    if "key_value" in value:
        out["keyValue"] = value["key_value"]
    out["count"] = value.get("count", 0)
    return out


def deserialize_json(data: dict) -> Bucket:
    out: Bucket = {}  # type: ignore[typeddict-item]
    if "keyValue" in data:
        out["key_value"] = data["keyValue"]
    if "count" in data:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
