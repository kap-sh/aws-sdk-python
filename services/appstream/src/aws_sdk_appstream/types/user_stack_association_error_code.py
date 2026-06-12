"""Generated from Smithy shape ``com.amazonaws.appstream#UserStackAssociationErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

UserStackAssociationErrorCode: TypeAlias = Literal[
    "STACK_NOT_FOUND",
    "USER_NAME_NOT_FOUND",
    "DIRECTORY_NOT_FOUND",
    "INTERNAL_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STACK_NOT_FOUND",
        "USER_NAME_NOT_FOUND",
        "DIRECTORY_NOT_FOUND",
        "INTERNAL_ERROR",
    )
)


def serialize_aws_json_1_1(value: UserStackAssociationErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserStackAssociationErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UserStackAssociationErrorCode value: {data!r}"
        )
    return cast(UserStackAssociationErrorCode, data)
