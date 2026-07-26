"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#Things``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.thing

Things: TypeAlias = list["capo_iotthingsgraph.types.thing.Thing"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Things) -> list:
    import capo_iotthingsgraph.types.thing

    out: list = []
    for item in value:
        out.append(capo_iotthingsgraph.types.thing.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Things:
    import capo_iotthingsgraph.types.thing

    out: Things = []
    for item in data:
        out.append(capo_iotthingsgraph.types.thing.deserialize_aws_json_1_1(item))
    return out
