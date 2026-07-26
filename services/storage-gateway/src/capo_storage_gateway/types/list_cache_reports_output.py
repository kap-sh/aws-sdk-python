"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListCacheReportsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.cache_report_list
    import capo_storage_gateway.types.marker


class ListCacheReportsOutput(TypedDict, closed=True):
    cache_report_list: NotRequired[
        "capo_storage_gateway.types.cache_report_list.CacheReportList"
    ]
    """<p>A list of existing cache reports for all file shares associated with your Amazon Web Services account. This list includes all information provided by the <code>DescribeCacheReport</code> action, such as report status, completion progress, start time, end time, filters, and tags.</p>"""
    marker: NotRequired["capo_storage_gateway.types.marker.Marker"]
    """<p>If the request includes <code>Marker</code>, the response returns that value in this field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCacheReportsOutput) -> dict:
    out: dict = {}
    if "cache_report_list" in value:
        import capo_storage_gateway.types.cache_report_list

        out["CacheReportList"] = (
            capo_storage_gateway.types.cache_report_list.serialize_aws_json_1_1(
                value["cache_report_list"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCacheReportsOutput:
    out: ListCacheReportsOutput = {}  # type: ignore[typeddict-item]
    if "CacheReportList" in data:
        import capo_storage_gateway.types.cache_report_list

        out["cache_report_list"] = (
            capo_storage_gateway.types.cache_report_list.deserialize_aws_json_1_1(
                data["CacheReportList"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
