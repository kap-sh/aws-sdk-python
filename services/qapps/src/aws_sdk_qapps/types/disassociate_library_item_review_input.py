"""Generated from Smithy shape ``com.amazonaws.qapps#DisassociateLibraryItemReviewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class DisassociateLibraryItemReviewInput(TypedDict, closed=True):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    library_item_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the library item to remove the review from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateLibraryItemReviewInput) -> dict:
    out: dict = {}
    out["libraryItemId"] = value["library_item_id"]
    return out


def deserialize_json(data: dict) -> DisassociateLibraryItemReviewInput:
    out: DisassociateLibraryItemReviewInput = {}  # type: ignore[typeddict-item]
    if "libraryItemId" in data:
        out["library_item_id"] = data["libraryItemId"]
    else:
        raise DeserializationError(
            "DisassociateLibraryItemReviewInput.library_item_id required"
        )
    return out
