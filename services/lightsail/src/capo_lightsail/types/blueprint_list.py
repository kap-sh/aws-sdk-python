"""Generated from Smithy shape ``com.amazonaws.lightsail#BlueprintList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.blueprint

BlueprintList: TypeAlias = list["capo_lightsail.types.blueprint.Blueprint"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueprintList) -> list:
    import capo_lightsail.types.blueprint

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.blueprint.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BlueprintList:
    import capo_lightsail.types.blueprint

    out: BlueprintList = []
    for item in data:
        out.append(capo_lightsail.types.blueprint.deserialize_aws_json_1_1(item))
    return out
