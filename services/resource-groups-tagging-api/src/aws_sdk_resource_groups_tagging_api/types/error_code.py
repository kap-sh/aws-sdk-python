"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups_tagging_api.errors import DeserializationError

ErrorCode: TypeAlias = Literal[
    "InternalServiceException",
    "InvalidParameterException",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InternalServiceException",
        "InvalidParameterException",
    )
)


def serialize_aws_json_1_1(value: ErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
