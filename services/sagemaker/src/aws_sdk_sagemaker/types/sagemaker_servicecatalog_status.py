"""Generated from Smithy shape ``com.amazonaws.sagemaker#SagemakerServicecatalogStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SagemakerServicecatalogStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_aws_json_1_1(value: SagemakerServicecatalogStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SagemakerServicecatalogStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SagemakerServicecatalogStatus value: {data!r}"
        )
    return cast(SagemakerServicecatalogStatus, data)
