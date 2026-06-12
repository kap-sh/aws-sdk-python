"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppNetworkAccessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AppNetworkAccessType: TypeAlias = Literal[
    "PublicInternetOnly",
    "VpcOnly",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PublicInternetOnly",
        "VpcOnly",
    )
)


def serialize_aws_json_1_1(value: AppNetworkAccessType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppNetworkAccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppNetworkAccessType value: {data!r}")
    return cast(AppNetworkAccessType, data)
