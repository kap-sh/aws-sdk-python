"""Generated from Smithy shape ``com.amazonaws.iot#UpdateThingTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.thing_type_name
    import capo_iot.types.thing_type_properties


class UpdateThingTypeRequest(TypedDict, closed=True):
    thing_type_name: "capo_iot.types.thing_type_name.ThingTypeName"
    """<p>The name of a thing type.</p>"""
    thing_type_properties: NotRequired[
        "capo_iot.types.thing_type_properties.ThingTypeProperties"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThingTypeRequest) -> dict:
    out: dict = {}
    if "thing_type_properties" in value:
        import capo_iot.types.thing_type_properties

        out["thingTypeProperties"] = (
            capo_iot.types.thing_type_properties.serialize_json(
                value["thing_type_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateThingTypeRequest:
    out: UpdateThingTypeRequest = {}  # type: ignore[typeddict-item]
    if "thingTypeProperties" in data:
        import capo_iot.types.thing_type_properties

        out["thing_type_properties"] = (
            capo_iot.types.thing_type_properties.deserialize_json(
                data["thingTypeProperties"]
            )
        )
    return out
