"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateLibraryItemInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.category_id_list
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.library_item_status
    import aws_sdk_qapps.types.uuid


class UpdateLibraryItemInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    library_item_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the library item to update.</p>"""
    status: NotRequired["aws_sdk_qapps.types.library_item_status.LibraryItemStatus"]
    """<p>The new status to set for the library item, such as \"Published\" or \"Hidden\".</p>"""
    categories: NotRequired["aws_sdk_qapps.types.category_id_list.CategoryIdList"]
    """<p>The new categories to associate with the library item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLibraryItemInput) -> dict:
    out: dict = {}
    out["libraryItemId"] = value["library_item_id"]
    if "status" in value:
        import aws_sdk_qapps.types.library_item_status

        out["status"] = aws_sdk_qapps.types.library_item_status.serialize_json(
            value["status"]
        )
    if "categories" in value:
        import aws_sdk_qapps.types.category_id_list

        out["categories"] = aws_sdk_qapps.types.category_id_list.serialize_json(
            value["categories"]
        )
    return out


def deserialize_json(data: dict) -> UpdateLibraryItemInput:
    out: UpdateLibraryItemInput = {}  # type: ignore[typeddict-item]
    if "libraryItemId" in data:
        out["library_item_id"] = data["libraryItemId"]
    else:
        raise DeserializationError("UpdateLibraryItemInput.library_item_id required")
    if "status" in data:
        import aws_sdk_qapps.types.library_item_status

        out["status"] = aws_sdk_qapps.types.library_item_status.deserialize_json(
            data["status"]
        )
    if "categories" in data:
        import aws_sdk_qapps.types.category_id_list

        out["categories"] = aws_sdk_qapps.types.category_id_list.deserialize_json(
            data["categories"]
        )
    return out
