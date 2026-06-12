"""Generated from Smithy shape ``com.amazonaws.storagegateway#StartCacheReportInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.cache_report_filter_list
    import aws_sdk_storage_gateway.types.client_token
    import aws_sdk_storage_gateway.types.dns_host_name
    import aws_sdk_storage_gateway.types.file_share_arn
    import aws_sdk_storage_gateway.types.location_arn
    import aws_sdk_storage_gateway.types.region_id
    import aws_sdk_storage_gateway.types.role
    import aws_sdk_storage_gateway.types.tags


class StartCacheReportInput(TypedDict):
    file_share_arn: "aws_sdk_storage_gateway.types.file_share_arn.FileShareARN"
    role: "aws_sdk_storage_gateway.types.role.Role"
    """<p>The ARN of the IAM role used when saving the cache report to Amazon S3.</p>"""
    location_arn: "aws_sdk_storage_gateway.types.location_arn.LocationARN"
    """<p>The ARN of the Amazon S3 bucket where you want to save the cache report.</p> <note> <p>We do not recommend saving the cache report to the same Amazon S3 bucket for which you are generating the report.</p> <p>This field does not accept access point ARNs.</p> </note>"""
    bucket_region: "aws_sdk_storage_gateway.types.region_id.RegionId"
    """<p>The Amazon Web Services Region of the Amazon S3 bucket where you want to save the cache report.</p>"""
    vpc_endpoint_dns_name: NotRequired[
        "aws_sdk_storage_gateway.types.dns_host_name.DNSHostName"
    ]
    """<p>The DNS name of the VPC endpoint associated with the Amazon S3 where you want to save the cache report. Optional.</p>"""
    inclusion_filters: NotRequired[
        "aws_sdk_storage_gateway.types.cache_report_filter_list.CacheReportFilterList"
    ]
    """<p>The list of filters and parameters that determine which files are included in the report. You must specify at least one value for <code>InclusionFilters</code> or <code>ExclusionFilters</code> in a <code>StartCacheReport</code> request.</p>"""
    exclusion_filters: NotRequired[
        "aws_sdk_storage_gateway.types.cache_report_filter_list.CacheReportFilterList"
    ]
    """<p>The list of filters and parameters that determine which files are excluded from the report. You must specify at least one value for <code>InclusionFilters</code> or <code>ExclusionFilters</code> in a <code>StartCacheReport</code> request.</p>"""
    client_token: "aws_sdk_storage_gateway.types.client_token.ClientToken"
    """<p>A unique identifier that you use to ensure idempotent report generation if you need to retry an unsuccessful <code>StartCacheReport</code> request. If you retry a request, use the same <code>ClientToken</code> you specified in the initial request.</p>"""
    tags: NotRequired["aws_sdk_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 key/value tags that you can assign to the cache report. Using tags can help you categorize your reports and more easily locate them in search results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCacheReportInput) -> dict:
    out: dict = {}
    out["FileShareARN"] = value["file_share_arn"]
    out["Role"] = value["role"]
    out["LocationARN"] = value["location_arn"]
    out["BucketRegion"] = value["bucket_region"]
    if "vpc_endpoint_dns_name" in value:
        out["VPCEndpointDNSName"] = value["vpc_endpoint_dns_name"]
    if "inclusion_filters" in value:
        import aws_sdk_storage_gateway.types.cache_report_filter_list

        out["InclusionFilters"] = (
            aws_sdk_storage_gateway.types.cache_report_filter_list.serialize_aws_json_1_1(
                value["inclusion_filters"]
            )
        )
    if "exclusion_filters" in value:
        import aws_sdk_storage_gateway.types.cache_report_filter_list

        out["ExclusionFilters"] = (
            aws_sdk_storage_gateway.types.cache_report_filter_list.serialize_aws_json_1_1(
                value["exclusion_filters"]
            )
        )
    out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_storage_gateway.types.tags

        out["Tags"] = aws_sdk_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCacheReportInput:
    out: StartCacheReportInput = {}  # type: ignore[typeddict-item]
    if "FileShareARN" in data:
        out["file_share_arn"] = data["FileShareARN"]
    else:
        raise DeserializationError("StartCacheReportInput.file_share_arn required")
    if "Role" in data:
        out["role"] = data["Role"]
    else:
        raise DeserializationError("StartCacheReportInput.role required")
    if "LocationARN" in data:
        out["location_arn"] = data["LocationARN"]
    else:
        raise DeserializationError("StartCacheReportInput.location_arn required")
    if "BucketRegion" in data:
        out["bucket_region"] = data["BucketRegion"]
    else:
        raise DeserializationError("StartCacheReportInput.bucket_region required")
    if "VPCEndpointDNSName" in data:
        out["vpc_endpoint_dns_name"] = data["VPCEndpointDNSName"]
    if "InclusionFilters" in data:
        import aws_sdk_storage_gateway.types.cache_report_filter_list

        out["inclusion_filters"] = (
            aws_sdk_storage_gateway.types.cache_report_filter_list.deserialize_aws_json_1_1(
                data["InclusionFilters"]
            )
        )
    if "ExclusionFilters" in data:
        import aws_sdk_storage_gateway.types.cache_report_filter_list

        out["exclusion_filters"] = (
            aws_sdk_storage_gateway.types.cache_report_filter_list.deserialize_aws_json_1_1(
                data["ExclusionFilters"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("StartCacheReportInput.client_token required")
    if "Tags" in data:
        import aws_sdk_storage_gateway.types.tags

        out["tags"] = aws_sdk_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
