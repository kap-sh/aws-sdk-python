"""Generated from Smithy shape ``com.amazonaws.managedblockchain#DeleteAccessorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string


class DeleteAccessorInput(TypedDict, closed=True):
    accessor_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the accessor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccessorInput:
    out: DeleteAccessorInput = {}  # type: ignore[typeddict-item]
    return out
