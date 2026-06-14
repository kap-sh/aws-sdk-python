"""Generated from Smithy shape ``com.amazonaws.workspaces#Tenancy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

Tenancy: TypeAlias = Literal[
    "DEDICATED",
    "SHARED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEDICATED",
        "SHARED",
    )
)


def serialize_aws_json_1_1(value: Tenancy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Tenancy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Tenancy value: {data!r}")
    return cast(Tenancy, data)
