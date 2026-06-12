"""Generated from Smithy shape ``com.amazonaws.sagemaker#IdleResourceSharing``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

IdleResourceSharing: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: IdleResourceSharing) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdleResourceSharing:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdleResourceSharing value: {data!r}")
    return cast(IdleResourceSharing, data)
