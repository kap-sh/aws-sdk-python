"""Generated from Smithy shape ``com.amazonaws.sagemaker#IsTrackingServerActive``."""

from typing import Literal, TypeAlias, cast

IsTrackingServerActive: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IsTrackingServerActive) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IsTrackingServerActive:
    return cast(IsTrackingServerActive, data)
