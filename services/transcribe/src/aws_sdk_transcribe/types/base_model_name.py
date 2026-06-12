"""Generated from Smithy shape ``com.amazonaws.transcribe#BaseModelName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

BaseModelName: TypeAlias = Literal[
    "NarrowBand",
    "WideBand",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NarrowBand",
        "WideBand",
    )
)


def serialize_aws_json_1_1(value: BaseModelName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BaseModelName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BaseModelName value: {data!r}")
    return cast(BaseModelName, data)
