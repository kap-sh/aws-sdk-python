"""Generated from Smithy shape ``com.amazonaws.appstream#FleetAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.fleet_attribute

FleetAttributes: TypeAlias = list["capo_appstream.types.fleet_attribute.FleetAttribute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetAttributes) -> list:
    import capo_appstream.types.fleet_attribute

    out: list = []
    for item in value:
        out.append(capo_appstream.types.fleet_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FleetAttributes:
    import capo_appstream.types.fleet_attribute

    out: FleetAttributes = []
    for item in data:
        out.append(capo_appstream.types.fleet_attribute.deserialize_aws_json_1_1(item))
    return out
