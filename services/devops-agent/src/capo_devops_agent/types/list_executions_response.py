"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.execution_list


class ListExecutionsResponse(TypedDict, closed=True):
    executions: "capo_devops_agent.types.execution_list.ExecutionList"
    """<p>List of executions</p>"""
    next_token: NotRequired["str"]
    """<p>Token for retrieving the next page of results, if available</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExecutionsResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.execution_list

    out["executions"] = capo_devops_agent.types.execution_list.serialize_json(
        value["executions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExecutionsResponse:
    out: ListExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "executions" in data:
        import capo_devops_agent.types.execution_list

        out["executions"] = capo_devops_agent.types.execution_list.deserialize_json(
            data["executions"]
        )
    else:
        raise DeserializationError("ListExecutionsResponse.executions required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
