"""Generated from Smithy shape ``com.amazonaws.sagemaker#CompleteOnConvergence``."""

from typing import Literal, TypeAlias, cast

CompleteOnConvergence: TypeAlias = Literal[
    "Disabled",
    "Enabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompleteOnConvergence) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompleteOnConvergence:
    return cast(CompleteOnConvergence, data)
