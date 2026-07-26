"""Generated from Smithy shape ``com.amazonaws.qapps#GetLibraryItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class GetLibraryItemInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    library_item_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the library item to retrieve.</p>"""
    app_id: NotRequired["capo_qapps.types.uuid.UUID"]
    """<p>The unique identifier of the Amazon Q App associated with the library item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLibraryItemInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLibraryItemInput:
    out: GetLibraryItemInput = {}  # type: ignore[typeddict-item]
    return out
