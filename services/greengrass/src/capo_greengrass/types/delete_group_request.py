"""Generated from Smithy shape ``com.amazonaws.greengrass#DeleteGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class DeleteGroupRequest(TypedDict, closed=True):
    group_id: "capo_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGroupRequest:
    out: DeleteGroupRequest = {}  # type: ignore[typeddict-item]
    return out
