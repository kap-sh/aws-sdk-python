"""Generated from Smithy shape ``com.amazonaws.sagemaker#EnabledOrDisabled``."""

from typing import Literal, TypeAlias, cast

EnabledOrDisabled: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnabledOrDisabled) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnabledOrDisabled:
    return cast(EnabledOrDisabled, data)
