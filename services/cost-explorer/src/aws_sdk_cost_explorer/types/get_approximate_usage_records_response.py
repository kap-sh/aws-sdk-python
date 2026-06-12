"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetApproximateUsageRecordsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.approximate_usage_records_per_service
    import aws_sdk_cost_explorer.types.date_interval
    import aws_sdk_cost_explorer.types.non_negative_long


class GetApproximateUsageRecordsResponse(TypedDict):
    services: NotRequired[
        "aws_sdk_cost_explorer.types.approximate_usage_records_per_service.ApproximateUsageRecordsPerService"
    ]
    """<p>The service metadata for the service or services in the response.</p>"""
    total_records: "aws_sdk_cost_explorer.types.non_negative_long.NonNegativeLong"
    """<p>The total number of usage records for all services in the services list.</p>"""
    lookback_period: NotRequired[
        "aws_sdk_cost_explorer.types.date_interval.DateInterval"
    ]
    """<p>The lookback period that's used for the estimation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApproximateUsageRecordsResponse) -> dict:
    out: dict = {}
    if "services" in value:
        import aws_sdk_cost_explorer.types.approximate_usage_records_per_service

        out["Services"] = (
            aws_sdk_cost_explorer.types.approximate_usage_records_per_service.serialize_aws_json_1_1(
                value["services"]
            )
        )
    out["TotalRecords"] = value.get("total_records", 0)
    if "lookback_period" in value:
        import aws_sdk_cost_explorer.types.date_interval

        out["LookbackPeriod"] = (
            aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
                value["lookback_period"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApproximateUsageRecordsResponse:
    out: GetApproximateUsageRecordsResponse = {}  # type: ignore[typeddict-item]
    if "Services" in data:
        import aws_sdk_cost_explorer.types.approximate_usage_records_per_service

        out["services"] = (
            aws_sdk_cost_explorer.types.approximate_usage_records_per_service.deserialize_aws_json_1_1(
                data["Services"]
            )
        )
    if "TotalRecords" in data:
        out["total_records"] = data["TotalRecords"]
    else:
        out["total_records"] = 0
    if "LookbackPeriod" in data:
        import aws_sdk_cost_explorer.types.date_interval

        out["lookback_period"] = (
            aws_sdk_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["LookbackPeriod"]
            )
        )
    return out
