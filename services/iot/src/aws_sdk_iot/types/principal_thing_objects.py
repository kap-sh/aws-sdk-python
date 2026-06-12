"""Generated from Smithy shape ``com.amazonaws.iot#PrincipalThingObjects``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.principal_thing_object

PrincipalThingObjects: TypeAlias = list[
    "aws_sdk_iot.types.principal_thing_object.PrincipalThingObject"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalThingObjects) -> list:
    import aws_sdk_iot.types.principal_thing_object

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.principal_thing_object.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrincipalThingObjects:
    import aws_sdk_iot.types.principal_thing_object

    out: PrincipalThingObjects = []
    for item in data:
        out.append(aws_sdk_iot.types.principal_thing_object.deserialize_json(item))
    return out
