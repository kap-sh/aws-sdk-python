"""Generated from Smithy shape ``com.amazonaws.marketplacecommerceanalytics#StartSupportDataExportResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_commerce_analytics.types.data_set_request_id


class StartSupportDataExportResult(TypedDict, closed=True):
    data_set_request_id: NotRequired[
        "capo_marketplace_commerce_analytics.types.data_set_request_id.DataSetRequestId"
    ]
    """<i>This target has been deprecated.</i> A unique identifier representing a specific request to the StartSupportDataExport operation. This identifier can be used to correlate a request with notifications from the SNS topic."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSupportDataExportResult) -> dict:
    out: dict = {}
    if "data_set_request_id" in value:
        out["dataSetRequestId"] = value["data_set_request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSupportDataExportResult:
    out: StartSupportDataExportResult = {}  # type: ignore[typeddict-item]
    if "dataSetRequestId" in data:
        out["data_set_request_id"] = data["dataSetRequestId"]
    return out
