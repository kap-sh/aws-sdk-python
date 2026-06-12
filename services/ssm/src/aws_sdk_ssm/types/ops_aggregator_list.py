"""Generated from Smithy shape ``com.amazonaws.ssm#OpsAggregatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_aggregator

OpsAggregatorList: TypeAlias = list["aws_sdk_ssm.types.ops_aggregator.OpsAggregator"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsAggregatorList) -> list:
    import aws_sdk_ssm.types.ops_aggregator

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.ops_aggregator.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsAggregatorList:
    import aws_sdk_ssm.types.ops_aggregator

    out: OpsAggregatorList = []
    for item in data:
        out.append(aws_sdk_ssm.types.ops_aggregator.deserialize_aws_json_1_1(item))
    return out
