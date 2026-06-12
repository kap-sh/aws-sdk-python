"""Generated from Smithy shape ``com.amazonaws.sagemaker#DirectInternetAccess``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

DirectInternetAccess: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: DirectInternetAccess) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectInternetAccess:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DirectInternetAccess value: {data!r}")
    return cast(DirectInternetAccess, data)
