"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessionArtifactType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

TestGridSessionArtifactType: TypeAlias = Literal[
    "UNKNOWN",
    "VIDEO",
    "SELENIUM_LOG",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNKNOWN",
        "VIDEO",
        "SELENIUM_LOG",
    )
)


def serialize_aws_json_1_1(value: TestGridSessionArtifactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TestGridSessionArtifactType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TestGridSessionArtifactType value: {data!r}"
        )
    return cast(TestGridSessionArtifactType, data)
