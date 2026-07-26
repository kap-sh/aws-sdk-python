"""Generated from Smithy shape ``com.amazonaws.iot#DeleteDynamicThingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.optional_version
    import capo_iot.types.thing_group_name


class DeleteDynamicThingGroupRequest(TypedDict, closed=True):
    thing_group_name: "capo_iot.types.thing_group_name.ThingGroupName"
    """<p>The name of the dynamic thing group to delete.</p>"""
    expected_version: NotRequired["capo_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the dynamic thing group to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDynamicThingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDynamicThingGroupRequest:
    out: DeleteDynamicThingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
