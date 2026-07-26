"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemsFilterOperator``."""

from typing import Literal, TypeAlias, cast

OpsItemRelatedItemsFilterOperator: TypeAlias = Literal["Equal",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemRelatedItemsFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemRelatedItemsFilterOperator:
    return cast(OpsItemRelatedItemsFilterOperator, data)
