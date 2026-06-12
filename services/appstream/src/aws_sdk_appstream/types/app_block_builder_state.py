"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

AppBlockBuilderState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "RUNNING",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: AppBlockBuilderState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppBlockBuilderState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppBlockBuilderState value: {data!r}")
    return cast(AppBlockBuilderState, data)
