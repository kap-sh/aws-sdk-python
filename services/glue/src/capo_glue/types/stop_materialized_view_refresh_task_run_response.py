"""Generated from Smithy shape ``com.amazonaws.glue#StopMaterializedViewRefreshTaskRunResponse``."""

from typing_extensions import TypedDict


class StopMaterializedViewRefreshTaskRunResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopMaterializedViewRefreshTaskRunResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopMaterializedViewRefreshTaskRunResponse:
    out: StopMaterializedViewRefreshTaskRunResponse = {}  # type: ignore[typeddict-item]
    return out
