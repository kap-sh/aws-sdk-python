"""Generated from Smithy shape ``com.amazonaws.managedblockchain#GetAccessorInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string


class GetAccessorInput(TypedDict):
    accessor_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the accessor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccessorInput:
    out: GetAccessorInput = {}  # type: ignore[typeddict-item]
    return out
