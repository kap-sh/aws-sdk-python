"""Generated from Smithy shape ``com.amazonaws.sagemaker#TtlDurationUnit``."""

from typing import Literal, TypeAlias, cast

TtlDurationUnit: TypeAlias = Literal[
    "Seconds",
    "Minutes",
    "Hours",
    "Days",
    "Weeks",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TtlDurationUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TtlDurationUnit:
    return cast(TtlDurationUnit, data)
