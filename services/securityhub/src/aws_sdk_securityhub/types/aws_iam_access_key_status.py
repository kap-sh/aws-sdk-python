"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamAccessKeyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

AwsIamAccessKeyStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
    )
)


def serialize_json(value: AwsIamAccessKeyStatus) -> str:
    return value


def deserialize_json(data: str) -> AwsIamAccessKeyStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AwsIamAccessKeyStatus value: {data!r}")
    return cast(AwsIamAccessKeyStatus, data)
