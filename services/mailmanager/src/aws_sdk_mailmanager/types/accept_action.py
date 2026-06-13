"""Generated from Smithy shape ``com.amazonaws.mailmanager#AcceptAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

AcceptAction: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_aws_json_1_0(value: AcceptAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AcceptAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceptAction value: {data!r}")
    return cast(AcceptAction, data)
