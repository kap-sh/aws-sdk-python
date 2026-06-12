"""Generated from Smithy shape ``com.amazonaws.fsx#Aliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.alias

Aliases: TypeAlias = list["aws_sdk_fsx.types.alias.Alias"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Aliases) -> list:
    import aws_sdk_fsx.types.alias

    out: list = []
    for item in value:
        out.append(aws_sdk_fsx.types.alias.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Aliases:
    import aws_sdk_fsx.types.alias

    out: Aliases = []
    for item in data:
        out.append(aws_sdk_fsx.types.alias.deserialize_aws_json_1_1(item))
    return out
