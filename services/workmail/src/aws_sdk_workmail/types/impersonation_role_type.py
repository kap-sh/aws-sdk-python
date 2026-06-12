"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationRoleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

ImpersonationRoleType: TypeAlias = Literal[
    "FULL_ACCESS",
    "READ_ONLY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_ACCESS",
        "READ_ONLY",
    )
)


def serialize_aws_json_1_1(value: ImpersonationRoleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImpersonationRoleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImpersonationRoleType value: {data!r}")
    return cast(ImpersonationRoleType, data)
