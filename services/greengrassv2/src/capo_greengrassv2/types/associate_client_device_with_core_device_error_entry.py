"""Generated from Smithy shape ``com.amazonaws.greengrassv2#AssociateClientDeviceWithCoreDeviceErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.io_t_thing_name
    import capo_greengrassv2.types.non_empty_string


class AssociateClientDeviceWithCoreDeviceErrorEntry(TypedDict, closed=True):
    thing_name: NotRequired["capo_greengrassv2.types.io_t_thing_name.IoTThingName"]
    """<p>The name of the IoT thing whose associate request failed.</p>"""
    code: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>The error code for the request.</p>"""
    message: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>A message that provides additional information about the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateClientDeviceWithCoreDeviceErrorEntry) -> dict:
    out: dict = {}
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AssociateClientDeviceWithCoreDeviceErrorEntry:
    out: AssociateClientDeviceWithCoreDeviceErrorEntry = {}  # type: ignore[typeddict-item]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
