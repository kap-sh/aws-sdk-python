"""Generated from Smithy shape ``com.amazonaws.lambda#InvocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

InvocationType: TypeAlias = Literal[
    "Event",
    "RequestResponse",
    "DryRun",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Event",
        "RequestResponse",
        "DryRun",
    )
)


def serialize_json(value: InvocationType) -> str:
    return value


def deserialize_json(data: str) -> InvocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InvocationType value: {data!r}")
    return cast(InvocationType, data)
