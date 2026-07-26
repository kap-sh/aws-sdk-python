"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyFeatureHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.clarify_header

ClarifyFeatureHeaders: TypeAlias = list[
    "capo_sagemaker.types.clarify_header.ClarifyHeader"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClarifyFeatureHeaders) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ClarifyFeatureHeaders:
    return list(data)
