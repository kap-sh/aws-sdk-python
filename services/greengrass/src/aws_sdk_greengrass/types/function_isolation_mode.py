"""Generated from Smithy shape ``com.amazonaws.greengrass#FunctionIsolationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

"""Specifies whether the Lambda function runs in a Greengrass container (default) or without containerization. Unless your scenario requires that you run without containerization, we recommend that you run in a Greengrass container. Omit this value to run the Lambda function with the default containerization for the group."""
FunctionIsolationMode: TypeAlias = Literal[
    "GreengrassContainer",
    "NoContainer",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GreengrassContainer",
        "NoContainer",
    )
)


def serialize_json(value: FunctionIsolationMode) -> str:
    return value


def deserialize_json(data: str) -> FunctionIsolationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FunctionIsolationMode value: {data!r}")
    return cast(FunctionIsolationMode, data)
