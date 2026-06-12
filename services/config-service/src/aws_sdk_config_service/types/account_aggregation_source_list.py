"""Generated from Smithy shape ``com.amazonaws.configservice#AccountAggregationSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_aggregation_source

AccountAggregationSourceList: TypeAlias = list[
    "aws_sdk_config_service.types.account_aggregation_source.AccountAggregationSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountAggregationSourceList) -> list:
    import aws_sdk_config_service.types.account_aggregation_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.account_aggregation_source.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccountAggregationSourceList:
    import aws_sdk_config_service.types.account_aggregation_source

    out: AccountAggregationSourceList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.account_aggregation_source.deserialize_aws_json_1_1(
                item
            )
        )
    return out
