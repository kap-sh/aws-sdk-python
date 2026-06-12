"""Generated from Smithy shape ``com.amazonaws.glue#ResourceAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ResourceAction: TypeAlias = Literal[
    "UPDATE",
    "CREATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATE",
        "CREATE",
    )
)


def serialize_aws_json_1_1(value: ResourceAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceAction value: {data!r}")
    return cast(ResourceAction, data)
