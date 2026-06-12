"""Generated from Smithy shape ``com.amazonaws.fms#RemediationActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

RemediationActionType: TypeAlias = Literal[
    "REMOVE",
    "MODIFY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REMOVE",
        "MODIFY",
    )
)


def serialize_aws_json_1_1(value: RemediationActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RemediationActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RemediationActionType value: {data!r}")
    return cast(RemediationActionType, data)
