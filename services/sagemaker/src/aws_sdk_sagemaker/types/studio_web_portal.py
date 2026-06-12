"""Generated from Smithy shape ``com.amazonaws.sagemaker#StudioWebPortal``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

StudioWebPortal: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: StudioWebPortal) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StudioWebPortal:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StudioWebPortal value: {data!r}")
    return cast(StudioWebPortal, data)
