"""Generated from Smithy shape ``com.amazonaws.quicksight#Sheet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_image_list
    import aws_sdk_quicksight.types.sheet_name
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class Sheet(TypedDict):
    sheet_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The unique identifier associated with a sheet.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.sheet_name.SheetName"]
    """<p>The name of a sheet. This name is displayed on the sheet's tab in the Quick Sight console.</p>"""
    images: NotRequired["aws_sdk_quicksight.types.sheet_image_list.SheetImageList"]
    """<p>A list of images on a sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sheet) -> dict:
    out: dict = {}
    if "sheet_id" in value:
        out["SheetId"] = value["sheet_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "images" in value:
        import aws_sdk_quicksight.types.sheet_image_list

        out["Images"] = aws_sdk_quicksight.types.sheet_image_list.serialize_json(
            value["images"]
        )
    return out


def deserialize_json(data: dict) -> Sheet:
    out: Sheet = {}  # type: ignore[typeddict-item]
    if "SheetId" in data:
        out["sheet_id"] = data["SheetId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Images" in data:
        import aws_sdk_quicksight.types.sheet_image_list

        out["images"] = aws_sdk_quicksight.types.sheet_image_list.deserialize_json(
            data["Images"]
        )
    return out
