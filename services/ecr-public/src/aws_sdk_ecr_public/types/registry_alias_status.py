"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RegistryAliasStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr_public.errors import DeserializationError

RegistryAliasStatus: TypeAlias = Literal[
    "ACTIVE",
    "PENDING",
    "REJECTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PENDING",
        "REJECTED",
    )
)


def serialize_aws_json_1_1(value: RegistryAliasStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegistryAliasStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegistryAliasStatus value: {data!r}")
    return cast(RegistryAliasStatus, data)
