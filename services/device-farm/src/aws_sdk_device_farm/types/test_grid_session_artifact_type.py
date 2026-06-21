"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessionArtifactType``."""

from typing import Literal, TypeAlias, cast

TestGridSessionArtifactType: TypeAlias = Literal[
    "UNKNOWN",
    "VIDEO",
    "SELENIUM_LOG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridSessionArtifactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TestGridSessionArtifactType:
    return cast(TestGridSessionArtifactType, data)
