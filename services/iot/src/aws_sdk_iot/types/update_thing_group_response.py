"""Generated from Smithy shape ``com.amazonaws.iot#UpdateThingGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.version


class UpdateThingGroupResponse(TypedDict):
    version: "aws_sdk_iot.types.version.Version"
    """<p>The version of the updated thing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThingGroupResponse) -> dict:
    out: dict = {}
    out["version"] = value.get("version", 0)
    return out


def deserialize_json(data: dict) -> UpdateThingGroupResponse:
    out: UpdateThingGroupResponse = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    return out
