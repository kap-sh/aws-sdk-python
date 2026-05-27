"""Generated from Smithy shape ``com.amazonaws.lambda#Runtime``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

Runtime: TypeAlias = Literal[
    "nodejs",
    "nodejs4.3",
    "nodejs6.10",
    "nodejs8.10",
    "nodejs10.x",
    "nodejs12.x",
    "nodejs14.x",
    "nodejs16.x",
    "java8",
    "java8.al2",
    "java11",
    "python2.7",
    "python3.6",
    "python3.7",
    "python3.8",
    "python3.9",
    "dotnetcore1.0",
    "dotnetcore2.0",
    "dotnetcore2.1",
    "dotnetcore3.1",
    "dotnet6",
    "dotnet8",
    "nodejs4.3-edge",
    "go1.x",
    "ruby2.5",
    "ruby2.7",
    "provided",
    "provided.al2",
    "nodejs18.x",
    "python3.10",
    "java17",
    "ruby3.2",
    "ruby3.3",
    "ruby3.4",
    "python3.11",
    "nodejs20.x",
    "provided.al2023",
    "python3.12",
    "java21",
    "python3.13",
    "nodejs22.x",
    "nodejs24.x",
    "python3.14",
    "java25",
    "dotnet10",
    "ruby4.0",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "nodejs",
        "nodejs4.3",
        "nodejs6.10",
        "nodejs8.10",
        "nodejs10.x",
        "nodejs12.x",
        "nodejs14.x",
        "nodejs16.x",
        "java8",
        "java8.al2",
        "java11",
        "python2.7",
        "python3.6",
        "python3.7",
        "python3.8",
        "python3.9",
        "dotnetcore1.0",
        "dotnetcore2.0",
        "dotnetcore2.1",
        "dotnetcore3.1",
        "dotnet6",
        "dotnet8",
        "nodejs4.3-edge",
        "go1.x",
        "ruby2.5",
        "ruby2.7",
        "provided",
        "provided.al2",
        "nodejs18.x",
        "python3.10",
        "java17",
        "ruby3.2",
        "ruby3.3",
        "ruby3.4",
        "python3.11",
        "nodejs20.x",
        "provided.al2023",
        "python3.12",
        "java21",
        "python3.13",
        "nodejs22.x",
        "nodejs24.x",
        "python3.14",
        "java25",
        "dotnet10",
        "ruby4.0",
    )
)


def serialize_json(value: Runtime) -> str:
    return value


def deserialize_json(data: str) -> Runtime:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Runtime value: {data!r}")
    return cast(Runtime, data)
