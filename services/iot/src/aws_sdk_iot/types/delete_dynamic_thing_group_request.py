"""Generated from Smithy shape ``com.amazonaws.iot#DeleteDynamicThingGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.optional_version
    import aws_sdk_iot.types.thing_group_name


class DeleteDynamicThingGroupRequest(TypedDict):
    thing_group_name: "aws_sdk_iot.types.thing_group_name.ThingGroupName"
    """<p>The name of the dynamic thing group to delete.</p>"""
    expected_version: NotRequired["aws_sdk_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the dynamic thing group to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDynamicThingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDynamicThingGroupRequest:
    out: DeleteDynamicThingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
