"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DeleteEntityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.state


class DeleteEntityResponse(TypedDict):
    state: "aws_sdk_iottwinmaker.types.state.State"
    """<p>The current state of the deleted entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEntityResponse) -> dict:
    out: dict = {}
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> DeleteEntityResponse:
    out: DeleteEntityResponse = {}  # type: ignore[typeddict-item]
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("DeleteEntityResponse.state required")
    return out
