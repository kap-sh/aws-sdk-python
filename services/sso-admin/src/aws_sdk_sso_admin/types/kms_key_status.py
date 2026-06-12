"""Generated from Smithy shape ``com.amazonaws.ssoadmin#KmsKeyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

KmsKeyStatus: TypeAlias = Literal[
    "UPDATING",
    "ENABLED",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATING",
        "ENABLED",
        "UPDATE_FAILED",
    )
)


def serialize_aws_json_1_1(value: KmsKeyStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KmsKeyStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KmsKeyStatus value: {data!r}")
    return cast(KmsKeyStatus, data)
