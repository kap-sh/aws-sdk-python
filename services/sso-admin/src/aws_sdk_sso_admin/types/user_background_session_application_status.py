"""Generated from Smithy shape ``com.amazonaws.ssoadmin#UserBackgroundSessionApplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

UserBackgroundSessionApplicationStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: UserBackgroundSessionApplicationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserBackgroundSessionApplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UserBackgroundSessionApplicationStatus value: {data!r}"
        )
    return cast(UserBackgroundSessionApplicationStatus, data)
