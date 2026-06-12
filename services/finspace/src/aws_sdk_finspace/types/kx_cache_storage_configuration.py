"""Generated from Smithy shape ``com.amazonaws.finspace#KxCacheStorageConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_cache_storage_size
    import aws_sdk_finspace.types.kx_cache_storage_type


class KxCacheStorageConfiguration(TypedDict):
    type: "aws_sdk_finspace.types.kx_cache_storage_type.KxCacheStorageType"
    """<p>The type of cache storage. The valid values are: </p> <ul> <li> <p>CACHE_1000 – This type provides at least 1000 MB/s disk access throughput. </p> </li> <li> <p>CACHE_250 – This type provides at least 250 MB/s disk access throughput. </p> </li> <li> <p>CACHE_12 – This type provides at least 12 MB/s disk access throughput. </p> </li> </ul> <p>For cache type <code>CACHE_1000</code> and <code>CACHE_250</code> you can select cache size as 1200 GB or increments of 2400 GB. For cache type <code>CACHE_12</code> you can select the cache size in increments of 6000 GB.</p>"""
    size: "aws_sdk_finspace.types.kx_cache_storage_size.KxCacheStorageSize"
    """<p>The size of cache in Gigabytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxCacheStorageConfiguration) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["size"] = value["size"]
    return out


def deserialize_json(data: dict) -> KxCacheStorageConfiguration:
    out: KxCacheStorageConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("KxCacheStorageConfiguration.type required")
    if "size" in data:
        out["size"] = data["size"]
    else:
        raise DeserializationError("KxCacheStorageConfiguration.size required")
    return out
