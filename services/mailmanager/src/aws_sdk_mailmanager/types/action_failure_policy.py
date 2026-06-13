"""Generated from Smithy shape ``com.amazonaws.mailmanager#ActionFailurePolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

ActionFailurePolicy: TypeAlias = Literal[
    "CONTINUE",
    "DROP",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTINUE",
        "DROP",
    )
)


def serialize_aws_json_1_0(value: ActionFailurePolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActionFailurePolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionFailurePolicy value: {data!r}")
    return cast(ActionFailurePolicy, data)
