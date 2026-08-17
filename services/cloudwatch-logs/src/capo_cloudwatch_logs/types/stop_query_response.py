"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StopQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.success


class StopQueryResponse(TypedDict, closed=True):
    success: "capo_cloudwatch_logs.types.success.Success"
    """<p>This is true if the query was stopped by the <code>StopQuery</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopQueryResponse) -> dict:
    out: dict = {}
    out["success"] = value.get("success", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> StopQueryResponse:
    out: StopQueryResponse = {}  # type: ignore[typeddict-item]
    if data.get("success") is not None:
        out["success"] = data["success"]
    else:
        out["success"] = False
    return out
