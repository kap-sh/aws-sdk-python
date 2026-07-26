"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomActionFilterOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.filter_operation_selected_fields_configuration
    import capo_quicksight.types.filter_operation_target_visuals_configuration


class CustomActionFilterOperation(TypedDict, closed=True):
    selected_fields_configuration: "capo_quicksight.types.filter_operation_selected_fields_configuration.FilterOperationSelectedFieldsConfiguration"
    """<p>The configuration that chooses the fields to be filtered.</p>"""
    target_visuals_configuration: "capo_quicksight.types.filter_operation_target_visuals_configuration.FilterOperationTargetVisualsConfiguration"
    """<p>The configuration that chooses the target visuals to be filtered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionFilterOperation) -> dict:
    out: dict = {}
    import capo_quicksight.types.filter_operation_selected_fields_configuration

    out["SelectedFieldsConfiguration"] = (
        capo_quicksight.types.filter_operation_selected_fields_configuration.serialize_json(
            value["selected_fields_configuration"]
        )
    )
    import capo_quicksight.types.filter_operation_target_visuals_configuration

    out["TargetVisualsConfiguration"] = (
        capo_quicksight.types.filter_operation_target_visuals_configuration.serialize_json(
            value["target_visuals_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomActionFilterOperation:
    out: CustomActionFilterOperation = {}  # type: ignore[typeddict-item]
    if "SelectedFieldsConfiguration" in data:
        import capo_quicksight.types.filter_operation_selected_fields_configuration

        out["selected_fields_configuration"] = (
            capo_quicksight.types.filter_operation_selected_fields_configuration.deserialize_json(
                data["SelectedFieldsConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CustomActionFilterOperation.selected_fields_configuration required"
        )
    if "TargetVisualsConfiguration" in data:
        import capo_quicksight.types.filter_operation_target_visuals_configuration

        out["target_visuals_configuration"] = (
            capo_quicksight.types.filter_operation_target_visuals_configuration.deserialize_json(
                data["TargetVisualsConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CustomActionFilterOperation.target_visuals_configuration required"
        )
    return out
