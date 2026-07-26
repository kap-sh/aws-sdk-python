"""Generated from Smithy shape ``com.amazonaws.gamelift#BuildList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.build

BuildList: TypeAlias = list["capo_gamelift.types.build.Build"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildList) -> list:
    import capo_gamelift.types.build

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.build.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BuildList:
    import capo_gamelift.types.build

    out: BuildList = []
    for item in data:
        out.append(capo_gamelift.types.build.deserialize_aws_json_1_1(item))
    return out
