"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateConformancePackComplianceSummaryFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_id
    import aws_sdk_config_service.types.aws_region


class AggregateConformancePackComplianceSummaryFilters(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_config_service.types.account_id.AccountId"]
    """<p>The 12-digit Amazon Web Services account ID of the source account.</p>"""
    aws_region: NotRequired["aws_sdk_config_service.types.aws_region.AwsRegion"]
    """<p>The source Amazon Web Services Region from where the data is aggregated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AggregateConformancePackComplianceSummaryFilters,
) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AggregateConformancePackComplianceSummaryFilters:
    out: AggregateConformancePackComplianceSummaryFilters = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    return out
