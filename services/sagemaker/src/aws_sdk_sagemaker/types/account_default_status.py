"""Generated from Smithy shape ``com.amazonaws.sagemaker#AccountDefaultStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AccountDefaultStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: AccountDefaultStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountDefaultStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountDefaultStatus value: {data!r}")
    return cast(AccountDefaultStatus, data)
