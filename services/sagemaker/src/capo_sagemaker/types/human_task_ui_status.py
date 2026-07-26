"""Generated from Smithy shape ``com.amazonaws.sagemaker#HumanTaskUiStatus``."""

from typing import Literal, TypeAlias, cast

HumanTaskUiStatus: TypeAlias = Literal[
    "Active",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanTaskUiStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HumanTaskUiStatus:
    return cast(HumanTaskUiStatus, data)
