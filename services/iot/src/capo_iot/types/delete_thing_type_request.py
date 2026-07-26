"""Generated from Smithy shape ``com.amazonaws.iot#DeleteThingTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.thing_type_name


class DeleteThingTypeRequest(TypedDict, closed=True):
    thing_type_name: "capo_iot.types.thing_type_name.ThingTypeName"
    """<p>The name of the thing type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThingTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteThingTypeRequest:
    out: DeleteThingTypeRequest = {}  # type: ignore[typeddict-item]
    return out
