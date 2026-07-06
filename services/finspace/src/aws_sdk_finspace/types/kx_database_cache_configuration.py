"""Generated from Smithy shape ``com.amazonaws.finspace#KxDatabaseCacheConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.db_paths
    import aws_sdk_finspace.types.kx_cache_storage_type
    import aws_sdk_finspace.types.kx_dataview_name


class KxDatabaseCacheConfiguration(TypedDict, closed=True):
    cache_type: "aws_sdk_finspace.types.kx_cache_storage_type.KxCacheStorageType"
    """<p>The type of disk cache. This parameter is used to map the database path to cache storage. The valid values are:</p> <ul> <li> <p>CACHE_1000 – This type provides at least 1000 MB/s disk access throughput. </p> </li> </ul>"""
    db_paths: "aws_sdk_finspace.types.db_paths.DbPaths"
    """<p>Specifies the portions of database that will be loaded into the cache for access.</p>"""
    dataview_name: NotRequired["aws_sdk_finspace.types.kx_dataview_name.KxDataviewName"]
    """<p> The name of the dataview to be used for caching historical data on disk. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxDatabaseCacheConfiguration) -> dict:
    out: dict = {}
    out["cacheType"] = value["cache_type"]
    import aws_sdk_finspace.types.db_paths

    out["dbPaths"] = aws_sdk_finspace.types.db_paths.serialize_json(value["db_paths"])
    if "dataview_name" in value:
        out["dataviewName"] = value["dataview_name"]
    return out


def deserialize_json(data: dict) -> KxDatabaseCacheConfiguration:
    out: KxDatabaseCacheConfiguration = {}  # type: ignore[typeddict-item]
    if "cacheType" in data:
        out["cache_type"] = data["cacheType"]
    else:
        raise DeserializationError("KxDatabaseCacheConfiguration.cache_type required")
    if "dbPaths" in data:
        import aws_sdk_finspace.types.db_paths

        out["db_paths"] = aws_sdk_finspace.types.db_paths.deserialize_json(
            data["dbPaths"]
        )
    else:
        raise DeserializationError("KxDatabaseCacheConfiguration.db_paths required")
    if "dataviewName" in data:
        out["dataview_name"] = data["dataviewName"]
    return out
