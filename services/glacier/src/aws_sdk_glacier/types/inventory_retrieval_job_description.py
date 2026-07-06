"""Generated from Smithy shape ``com.amazonaws.glacier#InventoryRetrievalJobDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.date_time
    import aws_sdk_glacier.types.string


class InventoryRetrievalJobDescription(TypedDict, closed=True):
    format: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The output format for the vault inventory list, which is set by the <b>InitiateJob</b> request when initiating a job to retrieve a vault inventory. Valid values are <code>CSV</code> and <code>JSON</code>.</p>"""
    start_date: NotRequired["aws_sdk_glacier.types.date_time.DateTime"]
    """<p>The start of the date range in Universal Coordinated Time (UTC) for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example <code>2013-03-20T17:03:43Z</code>.</p>"""
    end_date: NotRequired["aws_sdk_glacier.types.date_time.DateTime"]
    """<p>The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example <code>2013-03-20T17:03:43Z</code>.</p>"""
    limit: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The maximum number of inventory items returned per vault inventory retrieval request. This limit is set when initiating the job with the a <b>InitiateJob</b> request. </p>"""
    marker: NotRequired["aws_sdk_glacier.types.string.string"]
    r"""<p>An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new <b>InitiateJob</b> request to obtain additional inventory items. If there are no more inventory items, this value is <code>null</code>. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering\"> Range Inventory Retrieval</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InventoryRetrievalJobDescription) -> dict:
    out: dict = {}
    if "format" in value:
        out["Format"] = value["format"]
    if "start_date" in value:
        out["StartDate"] = value["start_date"]
    if "end_date" in value:
        out["EndDate"] = value["end_date"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> InventoryRetrievalJobDescription:
    out: InventoryRetrievalJobDescription = {}  # type: ignore[typeddict-item]
    if "Format" in data:
        out["format"] = data["Format"]
    if "StartDate" in data:
        out["start_date"] = data["StartDate"]
    if "EndDate" in data:
        out["end_date"] = data["EndDate"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
