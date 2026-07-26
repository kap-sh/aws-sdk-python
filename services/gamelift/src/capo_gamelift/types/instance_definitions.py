"""Generated from Smithy shape ``com.amazonaws.gamelift#InstanceDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.instance_definition

InstanceDefinitions: TypeAlias = list[
    "capo_gamelift.types.instance_definition.InstanceDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceDefinitions) -> list:
    import capo_gamelift.types.instance_definition

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.instance_definition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceDefinitions:
    import capo_gamelift.types.instance_definition

    out: InstanceDefinitions = []
    for item in data:
        out.append(
            capo_gamelift.types.instance_definition.deserialize_aws_json_1_1(item)
        )
    return out
