"""Generated from Smithy shape ``com.amazonaws.ecs#EFSAuthorizationConfigIAM``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

EFSAuthorizationConfigIAM: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: EFSAuthorizationConfigIAM) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EFSAuthorizationConfigIAM:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EFSAuthorizationConfigIAM value: {data!r}")
    return cast(EFSAuthorizationConfigIAM, data)
