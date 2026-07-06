"""Generated from Smithy shape ``com.amazonaws.omics#GetRunCacheResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.aws_account_id
    import aws_sdk_omics.types.cache_behavior
    import aws_sdk_omics.types.run_cache_arn
    import aws_sdk_omics.types.run_cache_id
    import aws_sdk_omics.types.run_cache_status
    import aws_sdk_omics.types.run_cache_timestamp
    import aws_sdk_omics.types.s3_uri_for_bucket_or_object
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.user_custom_description
    import aws_sdk_omics.types.user_custom_name


class GetRunCacheResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_omics.types.run_cache_arn.RunCacheArn"]
    """<p>Unique resource identifier for the run cache.</p>"""
    cache_behavior: NotRequired["aws_sdk_omics.types.cache_behavior.CacheBehavior"]
    """<p>The default cache behavior for runs using this cache.</p>"""
    cache_bucket_owner_id: NotRequired[
        "aws_sdk_omics.types.aws_account_id.AwsAccountId"
    ]
    """<p>The identifier of the bucket owner.</p>"""
    cache_s3_uri: NotRequired[
        "aws_sdk_omics.types.s3_uri_for_bucket_or_object.S3UriForBucketOrObject"
    ]
    """<p>The S3 URI where the cache data is stored.</p>"""
    creation_time: NotRequired[
        "aws_sdk_omics.types.run_cache_timestamp.RunCacheTimestamp"
    ]
    """<p>Creation time of the run cache (an ISO 8601 formatted string).</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.user_custom_description.UserCustomDescription"
    ]
    """<p>The run cache description.</p>"""
    id: NotRequired["aws_sdk_omics.types.run_cache_id.RunCacheId"]
    """<p>The run cache ID.</p>"""
    name: NotRequired["aws_sdk_omics.types.user_custom_name.UserCustomName"]
    """<p>The run cache name.</p>"""
    status: NotRequired["aws_sdk_omics.types.run_cache_status.RunCacheStatus"]
    """<p>The run cache status.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>The tags associated with the run cache.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRunCacheResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "cache_behavior" in value:
        out["cacheBehavior"] = value["cache_behavior"]
    if "cache_bucket_owner_id" in value:
        out["cacheBucketOwnerId"] = value["cache_bucket_owner_id"]
    if "cache_s3_uri" in value:
        out["cacheS3Uri"] = value["cache_s3_uri"]
    if "creation_time" in value:
        import aws_sdk_omics.types.run_cache_timestamp

        out["creationTime"] = aws_sdk_omics.types.run_cache_timestamp.serialize_json(
            value["creation_time"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetRunCacheResponse:
    out: GetRunCacheResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "cacheBehavior" in data:
        out["cache_behavior"] = data["cacheBehavior"]
    if "cacheBucketOwnerId" in data:
        out["cache_bucket_owner_id"] = data["cacheBucketOwnerId"]
    if "cacheS3Uri" in data:
        out["cache_s3_uri"] = data["cacheS3Uri"]
    if "creationTime" in data:
        import aws_sdk_omics.types.run_cache_timestamp

        out["creation_time"] = aws_sdk_omics.types.run_cache_timestamp.deserialize_json(
            data["creationTime"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    return out
