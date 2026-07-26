"""Generated from Smithy shape ``com.amazonaws.sagemaker#FairShare``."""

from typing import Literal, TypeAlias, cast

FairShare: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FairShare) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FairShare:
    return cast(FairShare, data)
