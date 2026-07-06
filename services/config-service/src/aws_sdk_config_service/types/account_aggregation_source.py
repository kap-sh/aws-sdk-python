"""Generated from Smithy shape ``com.amazonaws.configservice#AccountAggregationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_aggregation_source_account_list
    import aws_sdk_config_service.types.aggregator_region_list
    import aws_sdk_config_service.types.boolean


class AccountAggregationSource(TypedDict, closed=True):
    account_ids: "aws_sdk_config_service.types.account_aggregation_source_account_list.AccountAggregationSourceAccountList"
    """<p>The 12-digit account ID of the account being aggregated. </p>"""
    all_aws_regions: "aws_sdk_config_service.types.boolean.Boolean"
    """<p>If true, aggregate existing Config regions and future regions.</p>"""
    aws_regions: NotRequired[
        "aws_sdk_config_service.types.aggregator_region_list.AggregatorRegionList"
    ]
    """<p>The source regions being aggregated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountAggregationSource) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.account_aggregation_source_account_list

    out["AccountIds"] = (
        aws_sdk_config_service.types.account_aggregation_source_account_list.serialize_aws_json_1_1(
            value["account_ids"]
        )
    )
    out["AllAwsRegions"] = value.get("all_aws_regions", False)
    if "aws_regions" in value:
        import aws_sdk_config_service.types.aggregator_region_list

        out["AwsRegions"] = (
            aws_sdk_config_service.types.aggregator_region_list.serialize_aws_json_1_1(
                value["aws_regions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountAggregationSource:
    out: AccountAggregationSource = {}  # type: ignore[typeddict-item]
    if "AccountIds" in data:
        import aws_sdk_config_service.types.account_aggregation_source_account_list

        out["account_ids"] = (
            aws_sdk_config_service.types.account_aggregation_source_account_list.deserialize_aws_json_1_1(
                data["AccountIds"]
            )
        )
    else:
        raise DeserializationError("AccountAggregationSource.account_ids required")
    if "AllAwsRegions" in data:
        out["all_aws_regions"] = data["AllAwsRegions"]
    else:
        out["all_aws_regions"] = False
    if "AwsRegions" in data:
        import aws_sdk_config_service.types.aggregator_region_list

        out["aws_regions"] = (
            aws_sdk_config_service.types.aggregator_region_list.deserialize_aws_json_1_1(
                data["AwsRegions"]
            )
        )
    return out
