"""Generated from Smithy shape ``com.amazonaws.kendra#StartDataSourceSyncJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.string


class StartDataSourceSyncJobResponse(TypedDict, closed=True):
    execution_id: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>Identifies a particular synchronization job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDataSourceSyncJobResponse) -> dict:
    out: dict = {}
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDataSourceSyncJobResponse:
    out: StartDataSourceSyncJobResponse = {}  # type: ignore[typeddict-item]
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    return out
