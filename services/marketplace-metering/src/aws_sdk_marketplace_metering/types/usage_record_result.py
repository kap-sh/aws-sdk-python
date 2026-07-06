"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#UsageRecordResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.string
    import aws_sdk_marketplace_metering.types.usage_record
    import aws_sdk_marketplace_metering.types.usage_record_result_status


class UsageRecordResult(TypedDict, closed=True):
    usage_record: NotRequired[
        "aws_sdk_marketplace_metering.types.usage_record.UsageRecord"
    ]
    """<p>The <code>UsageRecord</code> that was part of the <code>BatchMeterUsage</code> request.</p>"""
    metering_record_id: NotRequired["aws_sdk_marketplace_metering.types.string.String"]
    """<p>The <code>MeteringRecordId</code> is a unique identifier for this metering event.</p>"""
    status: NotRequired[
        "aws_sdk_marketplace_metering.types.usage_record_result_status.UsageRecordResultStatus"
    ]
    """<p>The <code>UsageRecordResult</code> <code>Status</code> indicates the status of an individual <code>UsageRecord</code> processed by <code>BatchMeterUsage</code>.</p> <ul> <li> <p> <i>Success</i>- The <code>UsageRecord</code> was accepted and honored by <code>BatchMeterUsage</code>.</p> </li> <li> <p> <i>CustomerNotSubscribed</i>- The <code>CustomerIdentifier</code> specified is not able to use your product. The <code>UsageRecord</code> was not honored. There are three causes for this result:</p> <ul> <li> <p>The customer identifier is invalid.</p> </li> <li> <p>The customer identifier provided in the metering record does not have an active agreement or subscription with this product. Future <code>UsageRecords</code> for this customer will fail until the customer subscribes to your product.</p> </li> <li> <p>The customer's Amazon Web Services account was suspended.</p> </li> </ul> </li> <li> <p> <i>DuplicateRecord</i>- Indicates that the <code>UsageRecord</code> was invalid and not honored. A previously metered <code>UsageRecord</code> had the same customer, dimension, and time, but a different quantity.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageRecordResult) -> dict:
    out: dict = {}
    if "usage_record" in value:
        import aws_sdk_marketplace_metering.types.usage_record

        out["UsageRecord"] = (
            aws_sdk_marketplace_metering.types.usage_record.serialize_aws_json_1_1(
                value["usage_record"]
            )
        )
    if "metering_record_id" in value:
        out["MeteringRecordId"] = value["metering_record_id"]
    if "status" in value:
        import aws_sdk_marketplace_metering.types.usage_record_result_status

        out["Status"] = (
            aws_sdk_marketplace_metering.types.usage_record_result_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UsageRecordResult:
    out: UsageRecordResult = {}  # type: ignore[typeddict-item]
    if "UsageRecord" in data:
        import aws_sdk_marketplace_metering.types.usage_record

        out["usage_record"] = (
            aws_sdk_marketplace_metering.types.usage_record.deserialize_aws_json_1_1(
                data["UsageRecord"]
            )
        )
    if "MeteringRecordId" in data:
        out["metering_record_id"] = data["MeteringRecordId"]
    if "Status" in data:
        import aws_sdk_marketplace_metering.types.usage_record_result_status

        out["status"] = (
            aws_sdk_marketplace_metering.types.usage_record_result_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
