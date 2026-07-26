"""Generated from Smithy shape ``com.amazonaws.iot#ThingPrincipalObjects``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.thing_principal_object

ThingPrincipalObjects: TypeAlias = list[
    "capo_iot.types.thing_principal_object.ThingPrincipalObject"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThingPrincipalObjects) -> list:
    import capo_iot.types.thing_principal_object

    out: list = []
    for item in value:
        out.append(capo_iot.types.thing_principal_object.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThingPrincipalObjects:
    import capo_iot.types.thing_principal_object

    out: ThingPrincipalObjects = []
    for item in data:
        out.append(capo_iot.types.thing_principal_object.deserialize_json(item))
    return out
