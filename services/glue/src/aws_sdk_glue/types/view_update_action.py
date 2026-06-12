"""Generated from Smithy shape ``com.amazonaws.glue#ViewUpdateAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ViewUpdateAction: TypeAlias = Literal[
    "ADD",
    "REPLACE",
    "ADD_OR_REPLACE",
    "DROP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD",
        "REPLACE",
        "ADD_OR_REPLACE",
        "DROP",
    )
)


def serialize_aws_json_1_1(value: ViewUpdateAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ViewUpdateAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ViewUpdateAction value: {data!r}")
    return cast(ViewUpdateAction, data)
