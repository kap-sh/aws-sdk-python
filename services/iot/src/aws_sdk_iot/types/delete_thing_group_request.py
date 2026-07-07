"""Generated from Smithy shape ``com.amazonaws.iot#DeleteThingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.optional_version
    import aws_sdk_iot.types.thing_group_name


class DeleteThingGroupRequest(TypedDict, closed=True):
    thing_group_name: "aws_sdk_iot.types.thing_group_name.ThingGroupName"
    """<p>The name of the thing group to delete.</p>"""
    expected_version: NotRequired["aws_sdk_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the thing group to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteThingGroupRequest:
    out: DeleteThingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
