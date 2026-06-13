"""Generated from Smithy shape ``com.amazonaws.omics#RunCacheListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.cache_behavior
    import aws_sdk_omics.types.run_cache_arn
    import aws_sdk_omics.types.run_cache_id
    import aws_sdk_omics.types.run_cache_status
    import aws_sdk_omics.types.run_cache_timestamp
    import aws_sdk_omics.types.s3_uri_for_bucket_or_object
    import aws_sdk_omics.types.user_custom_name


class RunCacheListItem(TypedDict):
    arn: NotRequired["aws_sdk_omics.types.run_cache_arn.RunCacheArn"]
    """<p>Unique resource identifier for the run cache.</p>"""
    cache_behavior: NotRequired["aws_sdk_omics.types.cache_behavior.CacheBehavior"]
    """<p>Default cache behavior for the run cache.</p>"""
    cache_s3_uri: NotRequired[
        "aws_sdk_omics.types.s3_uri_for_bucket_or_object.S3UriForBucketOrObject"
    ]
    """<p>The S3 uri for the run cache data.</p>"""
    creation_time: NotRequired[
        "aws_sdk_omics.types.run_cache_timestamp.RunCacheTimestamp"
    ]
    """<p>The time that this run cache was created (an ISO 8601 formatted string).</p>"""
    id: NotRequired["aws_sdk_omics.types.run_cache_id.RunCacheId"]
    """<p>The identifier for this run cache.</p>"""
    name: NotRequired["aws_sdk_omics.types.user_custom_name.UserCustomName"]
    """<p>The name of the run cache.</p>"""
    status: NotRequired["aws_sdk_omics.types.run_cache_status.RunCacheStatus"]
    """<p>The run cache status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunCacheListItem) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "cache_behavior" in value:
        out["cacheBehavior"] = value["cache_behavior"]
    if "cache_s3_uri" in value:
        out["cacheS3Uri"] = value["cache_s3_uri"]
    if "creation_time" in value:
        import aws_sdk_omics.types.run_cache_timestamp

        out["creationTime"] = aws_sdk_omics.types.run_cache_timestamp.serialize_json(
            value["creation_time"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> RunCacheListItem:
    out: RunCacheListItem = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "cacheBehavior" in data:
        out["cache_behavior"] = data["cacheBehavior"]
    if "cacheS3Uri" in data:
        out["cache_s3_uri"] = data["cacheS3Uri"]
    if "creationTime" in data:
        import aws_sdk_omics.types.run_cache_timestamp

        out["creation_time"] = aws_sdk_omics.types.run_cache_timestamp.deserialize_json(
            data["creationTime"]
        )
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    return out
