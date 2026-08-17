"""Generated from Smithy shape ``com.amazonaws.ssm#OpsAggregatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_aggregator

OpsAggregatorList: TypeAlias = list["capo_ssm.types.ops_aggregator.OpsAggregator"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsAggregatorList) -> list:
    import capo_ssm.types.ops_aggregator

    out: list = []
    for item in value:
        out.append(capo_ssm.types.ops_aggregator.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsAggregatorList:
    import capo_ssm.types.ops_aggregator

    out: OpsAggregatorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.ops_aggregator.deserialize_aws_json_1_1(item))
    return out
