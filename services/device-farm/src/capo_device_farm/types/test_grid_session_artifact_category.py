"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessionArtifactCategory``."""

from typing import Literal, TypeAlias, cast

TestGridSessionArtifactCategory: TypeAlias = Literal[
    "VIDEO",
    "LOG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridSessionArtifactCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TestGridSessionArtifactCategory:
    return cast(TestGridSessionArtifactCategory, data)
