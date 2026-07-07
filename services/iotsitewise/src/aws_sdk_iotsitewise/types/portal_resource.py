"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class PortalResource(TypedDict, closed=True):
    id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the portal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortalResource) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> PortalResource:
    out: PortalResource = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("PortalResource.id required")
    return out
