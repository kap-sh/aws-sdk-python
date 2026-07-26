"""Generated from Smithy shape ``com.amazonaws.forecast#FeaturizationMethodName``."""

from typing import Literal, TypeAlias, cast

FeaturizationMethodName: TypeAlias = Literal["filling",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturizationMethodName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeaturizationMethodName:
    return cast(FeaturizationMethodName, data)
