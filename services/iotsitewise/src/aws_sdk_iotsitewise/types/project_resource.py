"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ProjectResource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class ProjectResource(TypedDict):
    id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectResource) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ProjectResource:
    out: ProjectResource = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ProjectResource.id required")
    return out
