"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.resource_status_value


class ResourceStatus(TypedDict, closed=True):
    name: NotRequired[
        "capo_resource_groups.types.resource_status_value.ResourceStatusValue"
    ]
    """<p>The current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatus) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_resource_groups.types.resource_status_value

        out["Name"] = capo_resource_groups.types.resource_status_value.serialize_json(
            value["name"]
        )
    return out


def deserialize_json(data: dict) -> ResourceStatus:
    out: ResourceStatus = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_resource_groups.types.resource_status_value

        out["name"] = capo_resource_groups.types.resource_status_value.deserialize_json(
            data["Name"]
        )
    return out
