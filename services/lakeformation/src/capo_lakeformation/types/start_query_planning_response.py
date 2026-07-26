"""Generated from Smithy shape ``com.amazonaws.lakeformation#StartQueryPlanningResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.query_id_string


class StartQueryPlanningResponse(TypedDict, closed=True):
    query_id: "capo_lakeformation.types.query_id_string.QueryIdString"
    """<p>The ID of the plan query operation can be used to fetch the actual work unit descriptors that are produced as the result of the operation. The ID is also used to get the query state and as an input to the <code>Execute</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryPlanningResponse) -> dict:
    out: dict = {}
    out["QueryId"] = value["query_id"]
    return out


def deserialize_json(data: dict) -> StartQueryPlanningResponse:
    out: StartQueryPlanningResponse = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    else:
        raise DeserializationError("StartQueryPlanningResponse.query_id required")
    return out
