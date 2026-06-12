"""Generated from Smithy shape ``com.amazonaws.sagemaker#RStudioServerProAccessStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RStudioServerProAccessStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: RStudioServerProAccessStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RStudioServerProAccessStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RStudioServerProAccessStatus value: {data!r}"
        )
    return cast(RStudioServerProAccessStatus, data)
