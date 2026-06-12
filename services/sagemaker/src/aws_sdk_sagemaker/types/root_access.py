"""Generated from Smithy shape ``com.amazonaws.sagemaker#RootAccess``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RootAccess: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: RootAccess) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RootAccess:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RootAccess value: {data!r}")
    return cast(RootAccess, data)
