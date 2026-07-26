"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceLevelObjectiveExclusionWindowsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.list_service_level_objective_exclusion_windows_max_results
    import capo_application_signals.types.next_token
    import capo_application_signals.types.service_level_objective_id


class ListServiceLevelObjectiveExclusionWindowsInput(TypedDict, closed=True):
    id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId"
    """<p>The ID of the SLO to list exclusion windows for.</p>"""
    max_results: NotRequired[
        "capo_application_signals.types.list_service_level_objective_exclusion_windows_max_results.ListServiceLevelObjectiveExclusionWindowsMaxResults"
    ]
    """<p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used. </p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of service level objectives. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceLevelObjectiveExclusionWindowsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServiceLevelObjectiveExclusionWindowsInput:
    out: ListServiceLevelObjectiveExclusionWindowsInput = {}  # type: ignore[typeddict-item]
    return out
