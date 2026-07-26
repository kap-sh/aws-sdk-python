"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#BatchMeterUsageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_metering.types.usage_record_list
    import capo_marketplace_metering.types.usage_record_result_list


class BatchMeterUsageResult(TypedDict, closed=True):
    results: NotRequired[
        "capo_marketplace_metering.types.usage_record_result_list.UsageRecordResultList"
    ]
    """<p>Contains all <code>UsageRecords</code> processed by <code>BatchMeterUsage</code>. These records were either honored by Amazon Web Services Marketplace Metering Service or were invalid. Invalid records should be fixed before being resubmitted.</p>"""
    unprocessed_records: NotRequired[
        "capo_marketplace_metering.types.usage_record_list.UsageRecordList"
    ]
    """<p>Contains all <code>UsageRecords</code> that were not processed by <code>BatchMeterUsage</code>. This is a list of <code>UsageRecords</code>. You can retry the failed request by making another <code>BatchMeterUsage</code> call with this list as input in the <code>BatchMeterUsageRequest</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchMeterUsageResult) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_marketplace_metering.types.usage_record_result_list

        out["Results"] = (
            capo_marketplace_metering.types.usage_record_result_list.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "unprocessed_records" in value:
        import capo_marketplace_metering.types.usage_record_list

        out["UnprocessedRecords"] = (
            capo_marketplace_metering.types.usage_record_list.serialize_aws_json_1_1(
                value["unprocessed_records"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchMeterUsageResult:
    out: BatchMeterUsageResult = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_marketplace_metering.types.usage_record_result_list

        out["results"] = (
            capo_marketplace_metering.types.usage_record_result_list.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    if "UnprocessedRecords" in data:
        import capo_marketplace_metering.types.usage_record_list

        out["unprocessed_records"] = (
            capo_marketplace_metering.types.usage_record_list.deserialize_aws_json_1_1(
                data["UnprocessedRecords"]
            )
        )
    return out
