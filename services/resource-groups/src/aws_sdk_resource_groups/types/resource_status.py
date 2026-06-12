"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.resource_status_value


class ResourceStatus(TypedDict):
    name: NotRequired[
        "aws_sdk_resource_groups.types.resource_status_value.ResourceStatusValue"
    ]
    """<p>The current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatus) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_resource_groups.types.resource_status_value

        out["Name"] = (
            aws_sdk_resource_groups.types.resource_status_value.serialize_json(
                value["name"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceStatus:
    out: ResourceStatus = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_resource_groups.types.resource_status_value

        out["name"] = (
            aws_sdk_resource_groups.types.resource_status_value.deserialize_json(
                data["Name"]
            )
        )
    return out
