"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalyResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.resource_name
    import capo_devops_guru.types.resource_type


class AnomalyResource(TypedDict, closed=True):
    name: NotRequired["capo_devops_guru.types.resource_name.ResourceName"]
    """<p>The name of the Amazon Web Services resource.</p>"""
    type: NotRequired["capo_devops_guru.types.resource_type.ResourceType"]
    """<p>The type of the Amazon Web Services resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyResource) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AnomalyResource:
    out: AnomalyResource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
