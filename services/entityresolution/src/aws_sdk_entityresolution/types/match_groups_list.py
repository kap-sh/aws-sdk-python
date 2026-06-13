"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.match_group

MatchGroupsList: TypeAlias = list[
    "aws_sdk_entityresolution.types.match_group.MatchGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchGroupsList) -> list:
    import aws_sdk_entityresolution.types.match_group

    out: list = []
    for item in value:
        out.append(aws_sdk_entityresolution.types.match_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchGroupsList:
    import aws_sdk_entityresolution.types.match_group

    out: MatchGroupsList = []
    for item in data:
        out.append(aws_sdk_entityresolution.types.match_group.deserialize_json(item))
    return out
