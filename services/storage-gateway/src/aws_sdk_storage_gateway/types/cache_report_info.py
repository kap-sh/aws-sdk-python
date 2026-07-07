"""Generated from Smithy shape ``com.amazonaws.storagegateway#CacheReportInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.cache_report_arn
    import aws_sdk_storage_gateway.types.cache_report_filter_list
    import aws_sdk_storage_gateway.types.cache_report_name
    import aws_sdk_storage_gateway.types.cache_report_status
    import aws_sdk_storage_gateway.types.file_share_arn
    import aws_sdk_storage_gateway.types.location_arn
    import aws_sdk_storage_gateway.types.report_completion_percent
    import aws_sdk_storage_gateway.types.role
    import aws_sdk_storage_gateway.types.tags
    import aws_sdk_storage_gateway.types.time


class CacheReportInfo(TypedDict, closed=True):
    cache_report_arn: NotRequired[
        "aws_sdk_storage_gateway.types.cache_report_arn.CacheReportARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the cache report you want to describe.</p>"""
    cache_report_status: NotRequired[
        "aws_sdk_storage_gateway.types.cache_report_status.CacheReportStatus"
    ]
    """<p>The status of the specified cache report.</p>"""
    report_completion_percent: NotRequired[
        "aws_sdk_storage_gateway.types.report_completion_percent.ReportCompletionPercent"
    ]
    """<p>The percentage of the report generation process that has been completed at time of inquiry.</p>"""
    end_time: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>The time at which the gateway stopped generating the cache report.</p>"""
    role: NotRequired["aws_sdk_storage_gateway.types.role.Role"]
    file_share_arn: NotRequired[
        "aws_sdk_storage_gateway.types.file_share_arn.FileShareARN"
    ]
    location_arn: NotRequired["aws_sdk_storage_gateway.types.location_arn.LocationARN"]
    """<p>The ARN of the Amazon S3 bucket location where the cache report is saved.</p>"""
    start_time: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>The time at which the gateway started generating the cache report.</p>"""
    inclusion_filters: NotRequired[
        "aws_sdk_storage_gateway.types.cache_report_filter_list.CacheReportFilterList"
    ]
    """<p>The list of filters and parameters that determine which files are included in the report.</p>"""
    exclusion_filters: NotRequired[
        "aws_sdk_storage_gateway.types.cache_report_filter_list.CacheReportFilterList"
    ]
    """<p>The list of filters and parameters that determine which files are excluded from the report.</p>"""
    report_name: NotRequired[
        "aws_sdk_storage_gateway.types.cache_report_name.CacheReportName"
    ]
    """<p>The file name of the completed cache report object stored in Amazon S3.</p>"""
    tags: NotRequired["aws_sdk_storage_gateway.types.tags.Tags"]
    """<p>The list of key/value tags associated with the report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheReportInfo) -> dict:
    out: dict = {}
    if "cache_report_arn" in value:
        out["CacheReportARN"] = value["cache_report_arn"]
    if "cache_report_status" in value:
        import aws_sdk_storage_gateway.types.cache_report_status

        out["CacheReportStatus"] = (
            aws_sdk_storage_gateway.types.cache_report_status.serialize_aws_json_1_1(
                value["cache_report_status"]
            )
        )
    if "report_completion_percent" in value:
        out["ReportCompletionPercent"] = value["report_completion_percent"]
    if "end_time" in value:
        import aws_sdk_storage_gateway.types.time

        out["EndTime"] = aws_sdk_storage_gateway.types.time.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "role" in value:
        out["Role"] = value["role"]
    if "file_share_arn" in value:
        out["FileShareARN"] = value["file_share_arn"]
    if "location_arn" in value:
        out["LocationARN"] = value["location_arn"]
    if "start_time" in value:
        import aws_sdk_storage_gateway.types.time

        out["StartTime"] = aws_sdk_storage_gateway.types.time.serialize_aws_json_1_1(
            value["start_time"]
        )
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
    if "report_name" in value:
        out["ReportName"] = value["report_name"]
    if "tags" in value:
        import aws_sdk_storage_gateway.types.tags

        out["Tags"] = aws_sdk_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CacheReportInfo:
    out: CacheReportInfo = {}  # type: ignore[typeddict-item]
    if "CacheReportARN" in data:
        out["cache_report_arn"] = data["CacheReportARN"]
    if "CacheReportStatus" in data:
        import aws_sdk_storage_gateway.types.cache_report_status

        out["cache_report_status"] = (
            aws_sdk_storage_gateway.types.cache_report_status.deserialize_aws_json_1_1(
                data["CacheReportStatus"]
            )
        )
    if "ReportCompletionPercent" in data:
        out["report_completion_percent"] = data["ReportCompletionPercent"]
    if "EndTime" in data:
        import aws_sdk_storage_gateway.types.time

        out["end_time"] = aws_sdk_storage_gateway.types.time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Role" in data:
        out["role"] = data["Role"]
    if "FileShareARN" in data:
        out["file_share_arn"] = data["FileShareARN"]
    if "LocationARN" in data:
        out["location_arn"] = data["LocationARN"]
    if "StartTime" in data:
        import aws_sdk_storage_gateway.types.time

        out["start_time"] = aws_sdk_storage_gateway.types.time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
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
    if "ReportName" in data:
        out["report_name"] = data["ReportName"]
    if "Tags" in data:
        import aws_sdk_storage_gateway.types.tags

        out["tags"] = aws_sdk_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
