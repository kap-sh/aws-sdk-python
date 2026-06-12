"""Generated from Smithy shape ``com.amazonaws.sagemaker#FairShare``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

FairShare: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: FairShare) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FairShare:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FairShare value: {data!r}")
    return cast(FairShare, data)
