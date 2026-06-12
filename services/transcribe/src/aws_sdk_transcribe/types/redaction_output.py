"""Generated from Smithy shape ``com.amazonaws.transcribe#RedactionOutput``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

RedactionOutput: TypeAlias = Literal[
    "redacted",
    "redacted_and_unredacted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "redacted",
        "redacted_and_unredacted",
    )
)


def serialize_aws_json_1_1(value: RedactionOutput) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RedactionOutput:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RedactionOutput value: {data!r}")
    return cast(RedactionOutput, data)
