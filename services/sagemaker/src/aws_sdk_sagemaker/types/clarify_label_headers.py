"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyLabelHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.clarify_header

ClarifyLabelHeaders: TypeAlias = list[
    "aws_sdk_sagemaker.types.clarify_header.ClarifyHeader"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClarifyLabelHeaders) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ClarifyLabelHeaders:
    return list(data)
