"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointStatusToUpdate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressPointStatusToUpdate: TypeAlias = Literal[
    "ACTIVE",
    "CLOSED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CLOSED",
    )
)


def serialize_aws_json_1_0(value: IngressPointStatusToUpdate) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressPointStatusToUpdate:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IngressPointStatusToUpdate value: {data!r}"
        )
    return cast(IngressPointStatusToUpdate, data)
