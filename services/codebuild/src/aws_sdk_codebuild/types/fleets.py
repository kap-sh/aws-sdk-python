"""Generated from Smithy shape ``com.amazonaws.codebuild#Fleets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.fleet

Fleets: TypeAlias = list["aws_sdk_codebuild.types.fleet.Fleet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Fleets) -> list:
    import aws_sdk_codebuild.types.fleet

    out: list = []
    for item in value:
        out.append(aws_sdk_codebuild.types.fleet.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Fleets:
    import aws_sdk_codebuild.types.fleet

    out: Fleets = []
    for item in data:
        out.append(aws_sdk_codebuild.types.fleet.deserialize_aws_json_1_1(item))
    return out
