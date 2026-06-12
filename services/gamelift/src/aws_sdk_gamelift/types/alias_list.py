"""Generated from Smithy shape ``com.amazonaws.gamelift#AliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.alias

AliasList: TypeAlias = list["aws_sdk_gamelift.types.alias.Alias"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AliasList) -> list:
    import aws_sdk_gamelift.types.alias

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.alias.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AliasList:
    import aws_sdk_gamelift.types.alias

    out: AliasList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.alias.deserialize_aws_json_1_1(item))
    return out
