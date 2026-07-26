"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisDefaults``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.default_new_sheet_configuration


class AnalysisDefaults(TypedDict, closed=True):
    default_new_sheet_configuration: "capo_quicksight.types.default_new_sheet_configuration.DefaultNewSheetConfiguration"
    """<p>The configuration for default new sheet settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisDefaults) -> dict:
    out: dict = {}
    import capo_quicksight.types.default_new_sheet_configuration

    out["DefaultNewSheetConfiguration"] = (
        capo_quicksight.types.default_new_sheet_configuration.serialize_json(
            value["default_new_sheet_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> AnalysisDefaults:
    out: AnalysisDefaults = {}  # type: ignore[typeddict-item]
    if "DefaultNewSheetConfiguration" in data:
        import capo_quicksight.types.default_new_sheet_configuration

        out["default_new_sheet_configuration"] = (
            capo_quicksight.types.default_new_sheet_configuration.deserialize_json(
                data["DefaultNewSheetConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AnalysisDefaults.default_new_sheet_configuration required"
        )
    return out
