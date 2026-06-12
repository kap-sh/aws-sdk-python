"""Generated from Smithy shape ``com.amazonaws.organizations#ActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

ActionType: TypeAlias = Literal[
    "INVITE",
    "ENABLE_ALL_FEATURES",
    "APPROVE_ALL_FEATURES",
    "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
    "TRANSFER_RESPONSIBILITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVITE",
        "ENABLE_ALL_FEATURES",
        "APPROVE_ALL_FEATURES",
        "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        "TRANSFER_RESPONSIBILITY",
    )
)


def serialize_aws_json_1_1(value: ActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionType value: {data!r}")
    return cast(ActionType, data)
