"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryPricingModel``."""

from typing import Literal, TypeAlias, cast

QueryPricingModel: TypeAlias = Literal[
    "BYTES_SCANNED",
    "COMPUTE_UNITS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryPricingModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> QueryPricingModel:
    return cast(QueryPricingModel, data)
