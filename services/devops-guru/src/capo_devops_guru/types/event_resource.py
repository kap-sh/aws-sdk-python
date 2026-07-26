"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.event_resource_arn
    import capo_devops_guru.types.event_resource_name
    import capo_devops_guru.types.event_resource_type


class EventResource(TypedDict, closed=True):
    type: NotRequired["capo_devops_guru.types.event_resource_type.EventResourceType"]
    """<p> The type of resource that emitted an event. </p>"""
    name: NotRequired["capo_devops_guru.types.event_resource_name.EventResourceName"]
    """<p> The name of the resource that emitted an event. </p>"""
    arn: NotRequired["capo_devops_guru.types.event_resource_arn.EventResourceArn"]
    """<p> The Amazon Resource Name (ARN) of the resource that emitted an event. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventResource) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> EventResource:
    out: EventResource = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
