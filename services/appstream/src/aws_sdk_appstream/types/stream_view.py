"""Generated from Smithy shape ``com.amazonaws.appstream#StreamView``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

StreamView: TypeAlias = Literal[
    "APP",
    "DESKTOP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APP",
        "DESKTOP",
    )
)


def serialize_aws_json_1_1(value: StreamView) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamView:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamView value: {data!r}")
    return cast(StreamView, data)
