"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldCustomTextContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.font_configuration
    import capo_quicksight.types.string


class TableFieldCustomTextContent(TypedDict, closed=True):
    value: NotRequired["capo_quicksight.types.string.String"]
    """<p>The string value of the custom text content for the table URL link content.</p>"""
    font_configuration: "capo_quicksight.types.font_configuration.FontConfiguration"
    """<p>The font configuration of the custom text content for the table URL link content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldCustomTextContent) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    import capo_quicksight.types.font_configuration

    out["FontConfiguration"] = capo_quicksight.types.font_configuration.serialize_json(
        value["font_configuration"]
    )
    return out


def deserialize_json(data: dict) -> TableFieldCustomTextContent:
    out: TableFieldCustomTextContent = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "FontConfiguration" in data:
        import capo_quicksight.types.font_configuration

        out["font_configuration"] = (
            capo_quicksight.types.font_configuration.deserialize_json(
                data["FontConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "TableFieldCustomTextContent.font_configuration required"
        )
    return out
