"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchUpdateExclusionWindowsErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.batch_update_exclusion_windows_error

BatchUpdateExclusionWindowsErrors: TypeAlias = list[
    "capo_application_signals.types.batch_update_exclusion_windows_error.BatchUpdateExclusionWindowsError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateExclusionWindowsErrors) -> list:
    import capo_application_signals.types.batch_update_exclusion_windows_error

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.batch_update_exclusion_windows_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateExclusionWindowsErrors:
    import capo_application_signals.types.batch_update_exclusion_windows_error

    out: BatchUpdateExclusionWindowsErrors = []
    for item in data:
        out.append(
            capo_application_signals.types.batch_update_exclusion_windows_error.deserialize_json(
                item
            )
        )
    return out
