"""Generated from Smithy shape ``com.amazonaws.glue#TriggerState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

TriggerState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "ACTIVATING",
    "ACTIVATED",
    "DEACTIVATING",
    "DEACTIVATED",
    "DELETING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "ACTIVATING",
        "ACTIVATED",
        "DEACTIVATING",
        "DEACTIVATED",
        "DELETING",
        "UPDATING",
    )
)


def serialize_aws_json_1_1(value: TriggerState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TriggerState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TriggerState value: {data!r}")
    return cast(TriggerState, data)
