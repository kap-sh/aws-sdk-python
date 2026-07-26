"""Generated from Smithy shape ``com.amazonaws.ssm#ParametersFilterKey``."""

from typing import Literal, TypeAlias, cast

ParametersFilterKey: TypeAlias = Literal[
    "Name",
    "Type",
    "KeyId",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParametersFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParametersFilterKey:
    return cast(ParametersFilterKey, data)
