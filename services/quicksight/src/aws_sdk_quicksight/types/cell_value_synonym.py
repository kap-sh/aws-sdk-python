"""Generated from Smithy shape ``com.amazonaws.quicksight#CellValueSynonym``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.string_list


class CellValueSynonym(TypedDict):
    cell_value: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The cell value.</p>"""
    synonyms: NotRequired["aws_sdk_quicksight.types.string_list.StringList"]
    """<p>Other names or aliases for the cell value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CellValueSynonym) -> dict:
    out: dict = {}
    if "cell_value" in value:
        out["CellValue"] = value["cell_value"]
    if "synonyms" in value:
        import aws_sdk_quicksight.types.string_list

        out["Synonyms"] = aws_sdk_quicksight.types.string_list.serialize_json(
            value["synonyms"]
        )
    return out


def deserialize_json(data: dict) -> CellValueSynonym:
    out: CellValueSynonym = {}  # type: ignore[typeddict-item]
    if "CellValue" in data:
        out["cell_value"] = data["CellValue"]
    if "Synonyms" in data:
        import aws_sdk_quicksight.types.string_list

        out["synonyms"] = aws_sdk_quicksight.types.string_list.deserialize_json(
            data["Synonyms"]
        )
    return out
