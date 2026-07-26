"""Generated from Smithy shape ``com.amazonaws.codebuild#Fleets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.fleet

Fleets: TypeAlias = list["capo_codebuild.types.fleet.Fleet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Fleets) -> list:
    import capo_codebuild.types.fleet

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.fleet.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Fleets:
    import capo_codebuild.types.fleet

    out: Fleets = []
    for item in data:
        out.append(capo_codebuild.types.fleet.deserialize_aws_json_1_1(item))
    return out
