"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssemblyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AssemblyType: TypeAlias = Literal[
    "None",
    "Line",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "Line",
    )
)


def serialize_aws_json_1_1(value: AssemblyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssemblyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssemblyType value: {data!r}")
    return cast(AssemblyType, data)
