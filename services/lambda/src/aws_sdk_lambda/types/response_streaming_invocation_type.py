"""Generated from Smithy shape ``com.amazonaws.lambda#ResponseStreamingInvocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

ResponseStreamingInvocationType: TypeAlias = Literal[
    "RequestResponse",
    "DryRun",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RequestResponse",
        "DryRun",
    )
)


def serialize_json(value: ResponseStreamingInvocationType) -> str:
    return value


def deserialize_json(data: str) -> ResponseStreamingInvocationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResponseStreamingInvocationType value: {data!r}"
        )
    return cast(ResponseStreamingInvocationType, data)
