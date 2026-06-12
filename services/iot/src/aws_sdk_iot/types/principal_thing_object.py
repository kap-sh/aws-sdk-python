"""Generated from Smithy shape ``com.amazonaws.iot#PrincipalThingObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_name
    import aws_sdk_iot.types.thing_principal_type


class PrincipalThingObject(TypedDict):
    thing_name: "aws_sdk_iot.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""
    thing_principal_type: NotRequired[
        "aws_sdk_iot.types.thing_principal_type.ThingPrincipalType"
    ]
    """<p>The type of the relation you want to specify when you attach a principal to a thing. The value defaults to <code>NON_EXCLUSIVE_THING</code>.</p> <ul> <li> <p> <code>EXCLUSIVE_THING</code> - Attaches the specified principal to the specified thing, exclusively. The thing will be the only thing that’s attached to the principal.</p> </li> </ul> <ul> <li> <p> <code>NON_EXCLUSIVE_THING</code> - Attaches the specified principal to the specified thing. Multiple things can be attached to the principal.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalThingObject) -> dict:
    out: dict = {}
    out["thingName"] = value["thing_name"]
    if "thing_principal_type" in value:
        import aws_sdk_iot.types.thing_principal_type

        out["thingPrincipalType"] = (
            aws_sdk_iot.types.thing_principal_type.serialize_json(
                value["thing_principal_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrincipalThingObject:
    out: PrincipalThingObject = {}  # type: ignore[typeddict-item]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    else:
        raise DeserializationError("PrincipalThingObject.thing_name required")
    if "thingPrincipalType" in data:
        import aws_sdk_iot.types.thing_principal_type

        out["thing_principal_type"] = (
            aws_sdk_iot.types.thing_principal_type.deserialize_json(
                data["thingPrincipalType"]
            )
        )
    return out
