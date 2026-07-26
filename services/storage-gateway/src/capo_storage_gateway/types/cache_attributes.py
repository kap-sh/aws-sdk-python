"""Generated from Smithy shape ``com.amazonaws.storagegateway#CacheAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.cache_stale_timeout_in_seconds


class CacheAttributes(TypedDict, closed=True):
    cache_stale_timeout_in_seconds: NotRequired[
        "capo_storage_gateway.types.cache_stale_timeout_in_seconds.CacheStaleTimeoutInSeconds"
    ]
    """<p>Refreshes a file share's cache by using Time To Live (TTL). TTL is the length of time since the last refresh after which access to the directory would cause the file gateway to first refresh that directory's contents from the Amazon S3 bucket or Amazon FSx file system. The TTL duration is in seconds.</p> <p>Valid Values:0, 300 to 2,592,000 seconds (5 minutes to 30 days)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheAttributes) -> dict:
    out: dict = {}
    if "cache_stale_timeout_in_seconds" in value:
        out["CacheStaleTimeoutInSeconds"] = value["cache_stale_timeout_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CacheAttributes:
    out: CacheAttributes = {}  # type: ignore[typeddict-item]
    if "CacheStaleTimeoutInSeconds" in data:
        out["cache_stale_timeout_in_seconds"] = data["CacheStaleTimeoutInSeconds"]
    return out
