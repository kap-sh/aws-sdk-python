"""Generated from Smithy shape ``com.amazonaws.medialive#FeatureActivations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.feature_activations_input_prepare_schedule_actions
    import aws_sdk_medialive.types.feature_activations_output_static_image_overlay_schedule_actions


class FeatureActivations(TypedDict, closed=True):
    input_prepare_schedule_actions: NotRequired[
        "aws_sdk_medialive.types.feature_activations_input_prepare_schedule_actions.FeatureActivationsInputPrepareScheduleActions"
    ]
    """Enables the Input Prepare feature. You can create Input Prepare actions in the schedule only if this feature is enabled. If you disable the feature on an existing schedule, make sure that you first delete all input prepare actions from the schedule."""
    output_static_image_overlay_schedule_actions: NotRequired[
        "aws_sdk_medialive.types.feature_activations_output_static_image_overlay_schedule_actions.FeatureActivationsOutputStaticImageOverlayScheduleActions"
    ]
    """Enables the output static image overlay feature. Enabling this feature allows you to send channel schedule updates to display/clear/modify image overlays on an output-by-output bases."""


# --- restJson1 ser/de ---
def serialize_json(value: FeatureActivations) -> dict:
    out: dict = {}
    if "input_prepare_schedule_actions" in value:
        import aws_sdk_medialive.types.feature_activations_input_prepare_schedule_actions

        out["inputPrepareScheduleActions"] = (
            aws_sdk_medialive.types.feature_activations_input_prepare_schedule_actions.serialize_json(
                value["input_prepare_schedule_actions"]
            )
        )
    if "output_static_image_overlay_schedule_actions" in value:
        import aws_sdk_medialive.types.feature_activations_output_static_image_overlay_schedule_actions

        out["outputStaticImageOverlayScheduleActions"] = (
            aws_sdk_medialive.types.feature_activations_output_static_image_overlay_schedule_actions.serialize_json(
                value["output_static_image_overlay_schedule_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> FeatureActivations:
    out: FeatureActivations = {}  # type: ignore[typeddict-item]
    if "inputPrepareScheduleActions" in data:
        import aws_sdk_medialive.types.feature_activations_input_prepare_schedule_actions

        out["input_prepare_schedule_actions"] = (
            aws_sdk_medialive.types.feature_activations_input_prepare_schedule_actions.deserialize_json(
                data["inputPrepareScheduleActions"]
            )
        )
    if "outputStaticImageOverlayScheduleActions" in data:
        import aws_sdk_medialive.types.feature_activations_output_static_image_overlay_schedule_actions

        out["output_static_image_overlay_schedule_actions"] = (
            aws_sdk_medialive.types.feature_activations_output_static_image_overlay_schedule_actions.deserialize_json(
                data["outputStaticImageOverlayScheduleActions"]
            )
        )
    return out
