"""Generated from Smithy shape ``com.amazonaws.iot#UpdateDynamicThingGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.version


class UpdateDynamicThingGroupResponse(TypedDict, closed=True):
    version: "capo_iot.types.version.Version"
    """<p>The dynamic thing group version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDynamicThingGroupResponse) -> dict:
    out: dict = {}
    out["version"] = value.get("version", 0)
    return out


def deserialize_json(data: dict) -> UpdateDynamicThingGroupResponse:
    out: UpdateDynamicThingGroupResponse = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    return out
