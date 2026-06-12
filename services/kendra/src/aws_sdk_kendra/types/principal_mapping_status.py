"""Generated from Smithy shape ``com.amazonaws.kendra#PrincipalMappingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

PrincipalMappingStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
    "PROCESSING",
    "DELETING",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "SUCCEEDED",
        "PROCESSING",
        "DELETING",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: PrincipalMappingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PrincipalMappingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrincipalMappingStatus value: {data!r}")
    return cast(PrincipalMappingStatus, data)
