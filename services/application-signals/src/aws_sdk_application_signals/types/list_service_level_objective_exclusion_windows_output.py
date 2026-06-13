"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceLevelObjectiveExclusionWindowsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.exclusion_windows
    import aws_sdk_application_signals.types.next_token


class ListServiceLevelObjectiveExclusionWindowsOutput(TypedDict):
    exclusion_windows: (
        "aws_sdk_application_signals.types.exclusion_windows.ExclusionWindows"
    )
    """<p>A list of exclusion windows configured for the SLO.</p>"""
    next_token: NotRequired["aws_sdk_application_signals.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of service level objectives. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceLevelObjectiveExclusionWindowsOutput) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.exclusion_windows

    out["ExclusionWindows"] = (
        aws_sdk_application_signals.types.exclusion_windows.serialize_json(
            value["exclusion_windows"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceLevelObjectiveExclusionWindowsOutput:
    out: ListServiceLevelObjectiveExclusionWindowsOutput = {}  # type: ignore[typeddict-item]
    if "ExclusionWindows" in data:
        import aws_sdk_application_signals.types.exclusion_windows

        out["exclusion_windows"] = (
            aws_sdk_application_signals.types.exclusion_windows.deserialize_json(
                data["ExclusionWindows"]
            )
        )
    else:
        raise DeserializationError(
            "ListServiceLevelObjectiveExclusionWindowsOutput.exclusion_windows required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
