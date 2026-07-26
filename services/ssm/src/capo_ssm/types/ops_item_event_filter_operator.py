"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemEventFilterOperator``."""

from typing import Literal, TypeAlias, cast

OpsItemEventFilterOperator: TypeAlias = Literal["Equal",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemEventFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemEventFilterOperator:
    return cast(OpsItemEventFilterOperator, data)
