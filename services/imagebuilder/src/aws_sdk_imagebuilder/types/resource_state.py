"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ResourceState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.resource_status


class ResourceState(TypedDict):
    status: NotRequired["aws_sdk_imagebuilder.types.resource_status.ResourceStatus"]
    """<p>Shows the current lifecycle policy action that was applied to an impacted resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceState) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_imagebuilder.types.resource_status

        out["status"] = aws_sdk_imagebuilder.types.resource_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> ResourceState:
    out: ResourceState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_imagebuilder.types.resource_status

        out["status"] = aws_sdk_imagebuilder.types.resource_status.deserialize_json(
            data["status"]
        )
    return out
