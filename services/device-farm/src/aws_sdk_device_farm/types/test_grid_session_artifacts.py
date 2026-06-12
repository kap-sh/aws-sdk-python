"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessionArtifacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.test_grid_session_artifact

TestGridSessionArtifacts: TypeAlias = list[
    "aws_sdk_device_farm.types.test_grid_session_artifact.TestGridSessionArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridSessionArtifacts) -> list:
    import aws_sdk_device_farm.types.test_grid_session_artifact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_device_farm.types.test_grid_session_artifact.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TestGridSessionArtifacts:
    import aws_sdk_device_farm.types.test_grid_session_artifact

    out: TestGridSessionArtifacts = []
    for item in data:
        out.append(
            aws_sdk_device_farm.types.test_grid_session_artifact.deserialize_aws_json_1_1(
                item
            )
        )
    return out
