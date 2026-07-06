"""Generated from Smithy shape ``com.amazonaws.marketplacecommerceanalytics#GenerateDataSetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_commerce_analytics.types.data_set_request_id


class GenerateDataSetResult(TypedDict, closed=True):
    data_set_request_id: NotRequired[
        "aws_sdk_marketplace_commerce_analytics.types.data_set_request_id.DataSetRequestId"
    ]
    """A unique identifier representing a specific request to the GenerateDataSet operation. This identifier can be used to correlate a request with notifications from the SNS topic."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateDataSetResult) -> dict:
    out: dict = {}
    if "data_set_request_id" in value:
        out["dataSetRequestId"] = value["data_set_request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateDataSetResult:
    out: GenerateDataSetResult = {}  # type: ignore[typeddict-item]
    if "dataSetRequestId" in data:
        out["data_set_request_id"] = data["dataSetRequestId"]
    return out
