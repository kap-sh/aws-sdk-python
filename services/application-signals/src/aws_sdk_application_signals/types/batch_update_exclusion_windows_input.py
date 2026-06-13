"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchUpdateExclusionWindowsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.exclusion_windows
    import aws_sdk_application_signals.types.service_level_objective_ids


class BatchUpdateExclusionWindowsInput(TypedDict):
    slo_ids: "aws_sdk_application_signals.types.service_level_objective_ids.ServiceLevelObjectiveIds"
    """<p>The list of SLO IDs to add or remove exclusion windows from.</p>"""
    add_exclusion_windows: NotRequired[
        "aws_sdk_application_signals.types.exclusion_windows.ExclusionWindows"
    ]
    """<p>A list of exclusion windows to add to the specified SLOs. You can add up to 10 exclusion windows per SLO.</p>"""
    remove_exclusion_windows: NotRequired[
        "aws_sdk_application_signals.types.exclusion_windows.ExclusionWindows"
    ]
    """<p>A list of exclusion windows to remove from the specified SLOs. The window configuration must match an existing exclusion window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateExclusionWindowsInput) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.service_level_objective_ids

    out["SloIds"] = (
        aws_sdk_application_signals.types.service_level_objective_ids.serialize_json(
            value["slo_ids"]
        )
    )
    if "add_exclusion_windows" in value:
        import aws_sdk_application_signals.types.exclusion_windows

        out["AddExclusionWindows"] = (
            aws_sdk_application_signals.types.exclusion_windows.serialize_json(
                value["add_exclusion_windows"]
            )
        )
    if "remove_exclusion_windows" in value:
        import aws_sdk_application_signals.types.exclusion_windows

        out["RemoveExclusionWindows"] = (
            aws_sdk_application_signals.types.exclusion_windows.serialize_json(
                value["remove_exclusion_windows"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateExclusionWindowsInput:
    out: BatchUpdateExclusionWindowsInput = {}  # type: ignore[typeddict-item]
    if "SloIds" in data:
        import aws_sdk_application_signals.types.service_level_objective_ids

        out["slo_ids"] = (
            aws_sdk_application_signals.types.service_level_objective_ids.deserialize_json(
                data["SloIds"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateExclusionWindowsInput.slo_ids required")
    if "AddExclusionWindows" in data:
        import aws_sdk_application_signals.types.exclusion_windows

        out["add_exclusion_windows"] = (
            aws_sdk_application_signals.types.exclusion_windows.deserialize_json(
                data["AddExclusionWindows"]
            )
        )
    if "RemoveExclusionWindows" in data:
        import aws_sdk_application_signals.types.exclusion_windows

        out["remove_exclusion_windows"] = (
            aws_sdk_application_signals.types.exclusion_windows.deserialize_json(
                data["RemoveExclusionWindows"]
            )
        )
    return out
