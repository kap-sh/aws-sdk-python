"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetVisualScopingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filter_visual_scope
    import aws_sdk_quicksight.types.filtered_visuals_list
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class SheetVisualScopingConfiguration(TypedDict):
    sheet_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The selected sheet that the filter is applied to.</p>"""
    scope: "aws_sdk_quicksight.types.filter_visual_scope.FilterVisualScope"
    """<p>The scope of the applied entities. Choose one of the following options:</p> <ul> <li> <p> <code>ALL_VISUALS</code> </p> </li> <li> <p> <code>SELECTED_VISUALS</code> </p> </li> </ul>"""
    visual_ids: NotRequired[
        "aws_sdk_quicksight.types.filtered_visuals_list.FilteredVisualsList"
    ]
    """<p>The selected visuals that the filter is applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetVisualScopingConfiguration) -> dict:
    out: dict = {}
    out["SheetId"] = value["sheet_id"]
    import aws_sdk_quicksight.types.filter_visual_scope

    out["Scope"] = aws_sdk_quicksight.types.filter_visual_scope.serialize_json(
        value["scope"]
    )
    if "visual_ids" in value:
        import aws_sdk_quicksight.types.filtered_visuals_list

        out["VisualIds"] = (
            aws_sdk_quicksight.types.filtered_visuals_list.serialize_json(
                value["visual_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetVisualScopingConfiguration:
    out: SheetVisualScopingConfiguration = {}  # type: ignore[typeddict-item]
    if "SheetId" in data:
        out["sheet_id"] = data["SheetId"]
    else:
        raise DeserializationError("SheetVisualScopingConfiguration.sheet_id required")
    if "Scope" in data:
        import aws_sdk_quicksight.types.filter_visual_scope

        out["scope"] = aws_sdk_quicksight.types.filter_visual_scope.deserialize_json(
            data["Scope"]
        )
    else:
        raise DeserializationError("SheetVisualScopingConfiguration.scope required")
    if "VisualIds" in data:
        import aws_sdk_quicksight.types.filtered_visuals_list

        out["visual_ids"] = (
            aws_sdk_quicksight.types.filtered_visuals_list.deserialize_json(
                data["VisualIds"]
            )
        )
    return out
