"""Generated from Smithy shape ``com.amazonaws.qbusiness#StartDataSourceSyncJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.execution_id


class StartDataSourceSyncJobResponse(TypedDict, closed=True):
    execution_id: NotRequired["capo_qbusiness.types.execution_id.ExecutionId"]
    """<p>The identifier for a particular synchronization job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDataSourceSyncJobResponse) -> dict:
    out: dict = {}
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    return out


def deserialize_json(data: dict) -> StartDataSourceSyncJobResponse:
    out: StartDataSourceSyncJobResponse = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    return out
