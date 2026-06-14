"""Generated from Smithy shape ``com.amazonaws.storagegateway#CacheReportFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.cache_report_filter_name
    import aws_sdk_storage_gateway.types.cache_report_filter_values


class CacheReportFilter(TypedDict):
    name: "aws_sdk_storage_gateway.types.cache_report_filter_name.CacheReportFilterName"
    """<p>The parameter name for a filter that determines which files are included or excluded from a cache report.</p> <p> <b>Valid Names:</b> </p> <p>UploadFailureReason | UploadState</p>"""
    values: "aws_sdk_storage_gateway.types.cache_report_filter_values.CacheReportFilterValues"
    """<p>The parameter value for a filter that determines which files are included or excluded from a cache report.</p> <p> <b>Valid <code>UploadFailureReason</code> Values:</b> </p> <p> <code>InaccessibleStorageClass</code> | <code>InvalidObjectState</code> | <code>ObjectMissing</code> | <code>S3AccessDenied</code> </p> <p> <b>Valid <code>UploadState</code> Values:</b> </p> <p> <code>FailingUpload</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheReportFilter) -> dict:
    out: dict = {}
    import aws_sdk_storage_gateway.types.cache_report_filter_name

    out["Name"] = (
        aws_sdk_storage_gateway.types.cache_report_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import aws_sdk_storage_gateway.types.cache_report_filter_values

    out["Values"] = (
        aws_sdk_storage_gateway.types.cache_report_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CacheReportFilter:
    out: CacheReportFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_storage_gateway.types.cache_report_filter_name

        out["name"] = (
            aws_sdk_storage_gateway.types.cache_report_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("CacheReportFilter.name required")
    if "Values" in data:
        import aws_sdk_storage_gateway.types.cache_report_filter_values

        out["values"] = (
            aws_sdk_storage_gateway.types.cache_report_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("CacheReportFilter.values required")
    return out
