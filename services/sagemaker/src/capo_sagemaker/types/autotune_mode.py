"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutotuneMode``."""

from typing import Literal, TypeAlias, cast

AutotuneMode: TypeAlias = Literal["Enabled",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutotuneMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutotuneMode:
    return cast(AutotuneMode, data)
