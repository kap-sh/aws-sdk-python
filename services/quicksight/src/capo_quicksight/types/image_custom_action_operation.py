"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageCustomActionOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.custom_action_navigation_operation
    import capo_quicksight.types.custom_action_set_parameters_operation
    import capo_quicksight.types.custom_action_url_operation


class ImageCustomActionOperation(TypedDict, closed=True):
    navigation_operation: NotRequired[
        "capo_quicksight.types.custom_action_navigation_operation.CustomActionNavigationOperation"
    ]
    url_operation: NotRequired[
        "capo_quicksight.types.custom_action_url_operation.CustomActionURLOperation"
    ]
    set_parameters_operation: NotRequired[
        "capo_quicksight.types.custom_action_set_parameters_operation.CustomActionSetParametersOperation"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ImageCustomActionOperation) -> dict:
    out: dict = {}
    if "navigation_operation" in value:
        import capo_quicksight.types.custom_action_navigation_operation

        out["NavigationOperation"] = (
            capo_quicksight.types.custom_action_navigation_operation.serialize_json(
                value["navigation_operation"]
            )
        )
    if "url_operation" in value:
        import capo_quicksight.types.custom_action_url_operation

        out["URLOperation"] = (
            capo_quicksight.types.custom_action_url_operation.serialize_json(
                value["url_operation"]
            )
        )
    if "set_parameters_operation" in value:
        import capo_quicksight.types.custom_action_set_parameters_operation

        out["SetParametersOperation"] = (
            capo_quicksight.types.custom_action_set_parameters_operation.serialize_json(
                value["set_parameters_operation"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImageCustomActionOperation:
    out: ImageCustomActionOperation = {}  # type: ignore[typeddict-item]
    if "NavigationOperation" in data:
        import capo_quicksight.types.custom_action_navigation_operation

        out["navigation_operation"] = (
            capo_quicksight.types.custom_action_navigation_operation.deserialize_json(
                data["NavigationOperation"]
            )
        )
    if "URLOperation" in data:
        import capo_quicksight.types.custom_action_url_operation

        out["url_operation"] = (
            capo_quicksight.types.custom_action_url_operation.deserialize_json(
                data["URLOperation"]
            )
        )
    if "SetParametersOperation" in data:
        import capo_quicksight.types.custom_action_set_parameters_operation

        out["set_parameters_operation"] = (
            capo_quicksight.types.custom_action_set_parameters_operation.deserialize_json(
                data["SetParametersOperation"]
            )
        )
    return out
