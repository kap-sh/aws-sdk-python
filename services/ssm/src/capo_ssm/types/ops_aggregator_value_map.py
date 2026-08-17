"""Generated from Smithy shape ``com.amazonaws.ssm#OpsAggregatorValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_aggregator_value
    import capo_ssm.types.ops_aggregator_value_key

OpsAggregatorValueMap: TypeAlias = dict[
    "capo_ssm.types.ops_aggregator_value_key.OpsAggregatorValueKey",
    "capo_ssm.types.ops_aggregator_value.OpsAggregatorValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: OpsAggregatorValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsAggregatorValueMap:
    out: OpsAggregatorValueMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
