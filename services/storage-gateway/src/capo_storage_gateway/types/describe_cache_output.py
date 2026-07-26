"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeCacheOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.disk_ids
    import capo_storage_gateway.types.double
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.long


class DescribeCacheOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    disk_ids: NotRequired["capo_storage_gateway.types.disk_ids.DiskIds"]
    """<p>An array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the <a>ListLocalDisks</a> API.</p>"""
    cache_allocated_in_bytes: "capo_storage_gateway.types.long.long"
    """<p>The amount of cache in bytes allocated to a gateway.</p>"""
    cache_used_percentage: "capo_storage_gateway.types.double.double"
    """<p>Percent use of the gateway's cache storage. This metric applies only to the gateway-cached volume setup. The sample is taken at the end of the reporting period.</p>"""
    cache_dirty_percentage: "capo_storage_gateway.types.double.double"
    """<p>The file share's contribution to the overall percentage of the gateway's cache that has not been persisted to Amazon Web Services. The sample is taken at the end of the reporting period.</p>"""
    cache_hit_percentage: "capo_storage_gateway.types.double.double"
    """<p>Percent of application read operations from the file shares that are served from cache. The sample is taken at the end of the reporting period.</p>"""
    cache_miss_percentage: "capo_storage_gateway.types.double.double"
    """<p>Percent of application read operations from the file shares that are not served from cache. The sample is taken at the end of the reporting period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCacheOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "disk_ids" in value:
        import capo_storage_gateway.types.disk_ids

        out["DiskIds"] = capo_storage_gateway.types.disk_ids.serialize_aws_json_1_1(
            value["disk_ids"]
        )
    out["CacheAllocatedInBytes"] = value.get("cache_allocated_in_bytes", 0)
    out["CacheUsedPercentage"] = value.get("cache_used_percentage", 0)
    out["CacheDirtyPercentage"] = value.get("cache_dirty_percentage", 0)
    out["CacheHitPercentage"] = value.get("cache_hit_percentage", 0)
    out["CacheMissPercentage"] = value.get("cache_miss_percentage", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCacheOutput:
    out: DescribeCacheOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "DiskIds" in data:
        import capo_storage_gateway.types.disk_ids

        out["disk_ids"] = capo_storage_gateway.types.disk_ids.deserialize_aws_json_1_1(
            data["DiskIds"]
        )
    if "CacheAllocatedInBytes" in data:
        out["cache_allocated_in_bytes"] = data["CacheAllocatedInBytes"]
    else:
        out["cache_allocated_in_bytes"] = 0
    if "CacheUsedPercentage" in data:
        out["cache_used_percentage"] = data["CacheUsedPercentage"]
    else:
        out["cache_used_percentage"] = 0
    if "CacheDirtyPercentage" in data:
        out["cache_dirty_percentage"] = data["CacheDirtyPercentage"]
    else:
        out["cache_dirty_percentage"] = 0
    if "CacheHitPercentage" in data:
        out["cache_hit_percentage"] = data["CacheHitPercentage"]
    else:
        out["cache_hit_percentage"] = 0
    if "CacheMissPercentage" in data:
        out["cache_miss_percentage"] = data["CacheMissPercentage"]
    else:
        out["cache_miss_percentage"] = 0
    return out
