"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ExclusionWindows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.exclusion_window

ExclusionWindows: TypeAlias = list[
    "aws_sdk_application_signals.types.exclusion_window.ExclusionWindow"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExclusionWindows) -> list:
    import aws_sdk_application_signals.types.exclusion_window

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_signals.types.exclusion_window.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExclusionWindows:
    import aws_sdk_application_signals.types.exclusion_window

    out: ExclusionWindows = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.exclusion_window.deserialize_json(item)
        )
    return out
