"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProfilingStatus``."""

from typing import Literal, TypeAlias, cast

ProfilingStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProfilingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProfilingStatus:
    return cast(ProfilingStatus, data)
