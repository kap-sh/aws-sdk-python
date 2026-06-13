"""Generated from Smithy shape ``com.amazonaws.braket#SearchQuantumTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.search_quantum_tasks_filter_list


class SearchQuantumTasksRequest(TypedDict):
    next_token: NotRequired["str"]
    """<p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>"""
    max_results: NotRequired["int"]
    """<p>Maximum number of results to return in the response.</p>"""
    filters: "aws_sdk_braket.types.search_quantum_tasks_filter_list.SearchQuantumTasksFilterList"
    """<p>Array of <code>SearchQuantumTasksFilter</code> objects to use when searching for quantum tasks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchQuantumTasksRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    import aws_sdk_braket.types.search_quantum_tasks_filter_list

    out["filters"] = (
        aws_sdk_braket.types.search_quantum_tasks_filter_list.serialize_json(
            value["filters"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchQuantumTasksRequest:
    out: SearchQuantumTasksRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filters" in data:
        import aws_sdk_braket.types.search_quantum_tasks_filter_list

        out["filters"] = (
            aws_sdk_braket.types.search_quantum_tasks_filter_list.deserialize_json(
                data["filters"]
            )
        )
    else:
        raise DeserializationError("SearchQuantumTasksRequest.filters required")
    return out
