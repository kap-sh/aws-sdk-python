"""Generated from Smithy shape ``com.amazonaws.sagemaker#CompleteOnConvergence``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CompleteOnConvergence: TypeAlias = Literal[
    "Disabled",
    "Enabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Disabled",
        "Enabled",
    )
)


def serialize_aws_json_1_1(value: CompleteOnConvergence) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompleteOnConvergence:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompleteOnConvergence value: {data!r}")
    return cast(CompleteOnConvergence, data)
