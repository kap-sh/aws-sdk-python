"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardVisualPublishOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.export_hidden_fields_option


class DashboardVisualPublishOptions(TypedDict, closed=True):
    export_hidden_fields_option: NotRequired[
        "capo_quicksight.types.export_hidden_fields_option.ExportHiddenFieldsOption"
    ]
    """<p>Determines if hidden fields are included in an exported dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardVisualPublishOptions) -> dict:
    out: dict = {}
    if "export_hidden_fields_option" in value:
        import capo_quicksight.types.export_hidden_fields_option

        out["ExportHiddenFieldsOption"] = (
            capo_quicksight.types.export_hidden_fields_option.serialize_json(
                value["export_hidden_fields_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashboardVisualPublishOptions:
    out: DashboardVisualPublishOptions = {}  # type: ignore[typeddict-item]
    if "ExportHiddenFieldsOption" in data:
        import capo_quicksight.types.export_hidden_fields_option

        out["export_hidden_fields_option"] = (
            capo_quicksight.types.export_hidden_fields_option.deserialize_json(
                data["ExportHiddenFieldsOption"]
            )
        )
    return out
