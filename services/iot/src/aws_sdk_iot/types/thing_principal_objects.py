"""Generated from Smithy shape ``com.amazonaws.iot#ThingPrincipalObjects``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_principal_object

ThingPrincipalObjects: TypeAlias = list[
    "aws_sdk_iot.types.thing_principal_object.ThingPrincipalObject"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThingPrincipalObjects) -> list:
    import aws_sdk_iot.types.thing_principal_object

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.thing_principal_object.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThingPrincipalObjects:
    import aws_sdk_iot.types.thing_principal_object

    out: ThingPrincipalObjects = []
    for item in data:
        out.append(aws_sdk_iot.types.thing_principal_object.deserialize_json(item))
    return out
