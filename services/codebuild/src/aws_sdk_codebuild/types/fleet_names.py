"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string

FleetNames: TypeAlias = list["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FleetNames:
    return list(data)
