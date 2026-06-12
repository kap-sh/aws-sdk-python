"""Generated from Smithy shape ``com.amazonaws.gamelift#InstanceDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.instance_definition

InstanceDefinitions: TypeAlias = list[
    "aws_sdk_gamelift.types.instance_definition.InstanceDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceDefinitions) -> list:
    import aws_sdk_gamelift.types.instance_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.instance_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceDefinitions:
    import aws_sdk_gamelift.types.instance_definition

    out: InstanceDefinitions = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.instance_definition.deserialize_aws_json_1_1(item)
        )
    return out
