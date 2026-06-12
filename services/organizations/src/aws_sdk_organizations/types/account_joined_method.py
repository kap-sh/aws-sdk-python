"""Generated from Smithy shape ``com.amazonaws.organizations#AccountJoinedMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

AccountJoinedMethod: TypeAlias = Literal[
    "INVITED",
    "CREATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVITED",
        "CREATED",
    )
)


def serialize_aws_json_1_1(value: AccountJoinedMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountJoinedMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountJoinedMethod value: {data!r}")
    return cast(AccountJoinedMethod, data)
