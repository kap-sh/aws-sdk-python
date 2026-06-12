"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomizationTechnique``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CustomizationTechnique: TypeAlias = Literal[
    "SFT",
    "DPO",
    "RLVR",
    "RLAIF",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SFT",
        "DPO",
        "RLVR",
        "RLAIF",
    )
)


def serialize_aws_json_1_1(value: CustomizationTechnique) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomizationTechnique:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomizationTechnique value: {data!r}")
    return cast(CustomizationTechnique, data)
