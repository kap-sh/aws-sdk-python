"""Generated from Smithy shape ``com.amazonaws.servicecatalog#PrincipalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

PrincipalType: TypeAlias = Literal[
    "IAM",
    "IAM_PATTERN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM",
        "IAM_PATTERN",
    )
)


def serialize_aws_json_1_1(value: PrincipalType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PrincipalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrincipalType value: {data!r}")
    return cast(PrincipalType, data)
