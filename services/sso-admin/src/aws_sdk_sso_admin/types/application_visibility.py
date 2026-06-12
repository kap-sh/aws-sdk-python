"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationVisibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

ApplicationVisibility: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]

DEFAULT_APPLICATION_VISIBILITY: ApplicationVisibility = "ENABLED"

# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ApplicationVisibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationVisibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationVisibility value: {data!r}")
    return cast(ApplicationVisibility, data)
