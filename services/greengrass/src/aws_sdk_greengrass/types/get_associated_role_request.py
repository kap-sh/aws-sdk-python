"""Generated from Smithy shape ``com.amazonaws.greengrass#GetAssociatedRoleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetAssociatedRoleRequest(TypedDict):
    group_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssociatedRoleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssociatedRoleRequest:
    out: GetAssociatedRoleRequest = {}  # type: ignore[typeddict-item]
    return out
