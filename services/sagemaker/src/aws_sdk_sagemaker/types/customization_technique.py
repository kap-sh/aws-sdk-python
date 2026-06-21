"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomizationTechnique``."""

from typing import Literal, TypeAlias, cast

CustomizationTechnique: TypeAlias = Literal[
    "SFT",
    "DPO",
    "RLVR",
    "RLAIF",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomizationTechnique) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomizationTechnique:
    return cast(CustomizationTechnique, data)
