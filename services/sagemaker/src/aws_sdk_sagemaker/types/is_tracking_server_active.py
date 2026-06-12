"""Generated from Smithy shape ``com.amazonaws.sagemaker#IsTrackingServerActive``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

IsTrackingServerActive: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
    )
)


def serialize_aws_json_1_1(value: IsTrackingServerActive) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IsTrackingServerActive:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsTrackingServerActive value: {data!r}")
    return cast(IsTrackingServerActive, data)
