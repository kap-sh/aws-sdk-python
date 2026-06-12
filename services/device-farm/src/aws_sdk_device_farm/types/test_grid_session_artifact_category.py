"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessionArtifactCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

TestGridSessionArtifactCategory: TypeAlias = Literal[
    "VIDEO",
    "LOG",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VIDEO",
        "LOG",
    )
)


def serialize_aws_json_1_1(value: TestGridSessionArtifactCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TestGridSessionArtifactCategory:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TestGridSessionArtifactCategory value: {data!r}"
        )
    return cast(TestGridSessionArtifactCategory, data)
