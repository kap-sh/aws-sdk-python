"""Generated from Smithy shape ``com.amazonaws.sagemaker#UltraServerHealthStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

UltraServerHealthStatus: TypeAlias = Literal[
    "OK",
    "Impaired",
    "Insufficient-Data",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OK",
        "Impaired",
        "Insufficient-Data",
    )
)


def serialize_aws_json_1_1(value: UltraServerHealthStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UltraServerHealthStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UltraServerHealthStatus value: {data!r}")
    return cast(UltraServerHealthStatus, data)
