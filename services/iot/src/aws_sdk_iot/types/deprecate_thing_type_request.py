"""Generated from Smithy shape ``com.amazonaws.iot#DeprecateThingTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_type_name
    import aws_sdk_iot.types.undo_deprecate


class DeprecateThingTypeRequest(TypedDict):
    thing_type_name: "aws_sdk_iot.types.thing_type_name.ThingTypeName"
    """<p>The name of the thing type to deprecate.</p>"""
    undo_deprecate: "aws_sdk_iot.types.undo_deprecate.UndoDeprecate"
    """<p>Whether to undeprecate a deprecated thing type. If <b>true</b>, the thing type will not be deprecated anymore and you can associate it with things.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeprecateThingTypeRequest) -> dict:
    out: dict = {}
    out["undoDeprecate"] = value.get("undo_deprecate", False)
    return out


def deserialize_json(data: dict) -> DeprecateThingTypeRequest:
    out: DeprecateThingTypeRequest = {}  # type: ignore[typeddict-item]
    if "undoDeprecate" in data:
        out["undo_deprecate"] = data["undoDeprecate"]
    else:
        out["undo_deprecate"] = False
    return out
