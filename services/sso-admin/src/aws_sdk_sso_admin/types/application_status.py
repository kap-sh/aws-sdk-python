"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

ApplicationStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ApplicationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationStatus value: {data!r}")
    return cast(ApplicationStatus, data)
