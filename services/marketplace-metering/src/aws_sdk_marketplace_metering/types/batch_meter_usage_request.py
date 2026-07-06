"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#BatchMeterUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_metering.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.product_code
    import aws_sdk_marketplace_metering.types.usage_record_list


class BatchMeterUsageRequest(TypedDict, closed=True):
    usage_records: (
        "aws_sdk_marketplace_metering.types.usage_record_list.UsageRecordList"
    )
    """<p>The set of <code>UsageRecords</code> to submit. <code>BatchMeterUsage</code> accepts up to 25 <code>UsageRecords</code> at a time.</p>"""
    product_code: "aws_sdk_marketplace_metering.types.product_code.ProductCode"
    """<p>Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchMeterUsageRequest) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_metering.types.usage_record_list

    out["UsageRecords"] = (
        aws_sdk_marketplace_metering.types.usage_record_list.serialize_aws_json_1_1(
            value["usage_records"]
        )
    )
    out["ProductCode"] = value.get("product_code", "")
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchMeterUsageRequest:
    out: BatchMeterUsageRequest = {}  # type: ignore[typeddict-item]
    if "UsageRecords" in data:
        import aws_sdk_marketplace_metering.types.usage_record_list

        out["usage_records"] = (
            aws_sdk_marketplace_metering.types.usage_record_list.deserialize_aws_json_1_1(
                data["UsageRecords"]
            )
        )
    else:
        raise DeserializationError("BatchMeterUsageRequest.usage_records required")
    if "ProductCode" in data:
        out["product_code"] = data["ProductCode"]
    else:
        out["product_code"] = ""
    return out
