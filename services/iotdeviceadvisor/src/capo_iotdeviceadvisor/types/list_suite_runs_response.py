"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#ListSuiteRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.suite_runs_list
    import capo_iotdeviceadvisor.types.token


class ListSuiteRunsResponse(TypedDict, closed=True):
    suite_runs_list: NotRequired[
        "capo_iotdeviceadvisor.types.suite_runs_list.SuiteRunsList"
    ]
    """<p>An array of objects that provide summaries of information about the suite runs in the list.</p>"""
    next_token: NotRequired["capo_iotdeviceadvisor.types.token.Token"]
    """<p>A token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSuiteRunsResponse) -> dict:
    out: dict = {}
    if "suite_runs_list" in value:
        import capo_iotdeviceadvisor.types.suite_runs_list

        out["suiteRunsList"] = (
            capo_iotdeviceadvisor.types.suite_runs_list.serialize_json(
                value["suite_runs_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSuiteRunsResponse:
    out: ListSuiteRunsResponse = {}  # type: ignore[typeddict-item]
    if "suiteRunsList" in data:
        import capo_iotdeviceadvisor.types.suite_runs_list

        out["suite_runs_list"] = (
            capo_iotdeviceadvisor.types.suite_runs_list.deserialize_json(
                data["suiteRunsList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
