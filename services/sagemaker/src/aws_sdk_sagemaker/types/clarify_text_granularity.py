"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyTextGranularity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClarifyTextGranularity: TypeAlias = Literal[
    "token",
    "sentence",
    "paragraph",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "token",
        "sentence",
        "paragraph",
    )
)


def serialize_aws_json_1_1(value: ClarifyTextGranularity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClarifyTextGranularity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClarifyTextGranularity value: {data!r}")
    return cast(ClarifyTextGranularity, data)
