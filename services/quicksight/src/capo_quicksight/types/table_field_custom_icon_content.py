"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldCustomIconContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.table_field_icon_set_type


class TableFieldCustomIconContent(TypedDict, closed=True):
    icon: NotRequired[
        "capo_quicksight.types.table_field_icon_set_type.TableFieldIconSetType"
    ]
    """<p>The icon set type (link) of the custom icon content for table URL link content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldCustomIconContent) -> dict:
    out: dict = {}
    if "icon" in value:
        import capo_quicksight.types.table_field_icon_set_type

        out["Icon"] = capo_quicksight.types.table_field_icon_set_type.serialize_json(
            value["icon"]
        )
    return out


def deserialize_json(data: dict) -> TableFieldCustomIconContent:
    out: TableFieldCustomIconContent = {}  # type: ignore[typeddict-item]
    if "Icon" in data:
        import capo_quicksight.types.table_field_icon_set_type

        out["icon"] = capo_quicksight.types.table_field_icon_set_type.deserialize_json(
            data["Icon"]
        )
    return out
