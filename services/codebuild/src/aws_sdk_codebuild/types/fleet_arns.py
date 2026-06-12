"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string

FleetArns: TypeAlias = list["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FleetArns:
    return list(data)
